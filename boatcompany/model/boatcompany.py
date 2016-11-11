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
import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression  # V7
from openerp import models, fields, api, _  # v8
from openerp.exceptions import except_orm, UserError, ValidationError

import re
import time
import datetime
from datetime import datetime
from time import gmtime, strftime

class product_template(models.Model):
    _inherit = 'product.template'

    boatlength = fields.Char('Boat Length:',size=10)
    fieldcapacity = fields.Char('Field Capacity:',size=10)
    modeloptionsid = fields.Many2one('product.category','Model Options:')

class product_product(models.Model):
    _inherit = 'product.product'

    def _search(self, cr, user, args, offset=0, limit=None, order=None, context=None, count=False,access_rights_uid=None):
        print "Inside Search==============================="
        if context is None:
            context = {}
        if context.get('boatmodelid'):
            print "contetx==============",context
            local = context.get('boatmodelid')
            a = self.pool.get('product.template').browse(cr, user, local , context=context)
            print "a=================",a
            args = [('categ_id', '=', a['modeloptionsid'].id)] + args
            print "Args===================",args
        return super(product_product, self)._search(cr, user, args, offset, limit, order, context, count, access_rights_uid)


class sale_order(models.Model):
    _inherit = 'sale.order'

    boatmodelid = fields.Many2one('product.template','Boat Model:',domain=[('categ_id.name','=','Boat Models')])


