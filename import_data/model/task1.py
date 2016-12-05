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


class res_users(models.Model):
    _name = 'res.users'
    _inherit = ['res.users', 'mail.thread']

    commission_field = fields.Float('Commission :')

    @api.model
    def create(self,fields):
        print "FIELDS CREATE=============================="
        var = fields.get('commission_field',0)
        print "FIELDS CREATE=====================",var
        print "FIELDS CREATE=====================",type(var)
        if 1 <= var <= 5:
            pass
        else:
            raise except_orm(_("Values Should be Between 1 to 5 Only!!!"))
        return super(res_users, self).create(fields)

    # @api.multi
    # def write(self,vals):
    #     print "FIELDS WRITE=============================="
    #     var = vals.get('commission_field',0)
    #     print "FIELDS WRITE=====================",var
    #     if var>=1 and var<=5:
    #         pass
    #     else:
    #         raise except_orm(_("Values Should be Between 1 to 5 Only!!!"))
    #
    #     print "SELF===============================",self.commission_field
    #     print "SELF===============================",self.name
    #     print "VALS===============================",vals['commission_field']
    #     print "CONTXT========================",self._context.get('params')['id']
    #     my_id = self._context.get('params')['id']
    #     record_id = self.env['res.users'].browse(my_id)
    #     print "record", record_id
    #
    #     log_message = _('Options changed for %s i.e %s ->> %s' % (self.name, self.commission_field, vals['commission_field']))
    #     a = record_id.message_post(body=log_message, type='comment', author_id=record_id.partner_id.id, attachments=[])
    #     print "a", a
    #     if a:
    #         a.write({'res_id': my_id, 'model': 'res.users'})
    #     return super(res_users, self).write(vals)

    # bom_id.message_post(log_message, type='comment', author_id=uid_brw.partner_id.id, attachments=[])

class sale_order_inherit(models.Model):
    _inherit = 'sale.order'

    commission_field = fields.Float('Commission Field:',default='0.00')

    # @api.model
    # def create(self,vals):
    #     my_id = vals['user_id']
    #     record = self.env['res.users'].browse(my_id)
    #     value = record.commission_field
    #     vals['commission_field'] = value
    #     return super(sale_order_inherit, self).create(vals)
    #



