# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from gtk.keysyms import cr

from openerp.osv import fields, osv, expression  # V7
from openerp import models, fields, api, _  # v8
import base64
import xlrd
from datetime import datetime
import calendar
import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8
from openerp.exceptions import except_orm,UserError, ValidationError



class sale_order_custom_inherit(models.TransientModel):
    _name = 'sale.order.custom.inherit'

    local = fields.Char('Local')

    @api.multi
    def Confirm_sale(self):
        record = self._context.get('active_ids')
        counter = 0
        print "LENGTH======================",len(record)
        for each in record:
            rec = self.env['sale.order'].browse(each)
            if rec.state == 'draft':
                rec.action_confirm()
                new_rec = self.env['sale.advance.payment.inv'].create({'advance_payment_method':'percentage','amount':rec.amount_total}).create_invoices()
                my_rec = self.env['account.invoice'].search([('origin','=',rec.name)])
                my_rec.signal_workflow('invoice_open')
            elif rec.state == 'cancel':
                counter += 1
                continue
            else:
                raise except_orm(_('NOT In Draft Stage'))
        if len(record) == counter:
            raise except_orm(_("ALL ARE IN CANCELLED STATE"))
        return rec
