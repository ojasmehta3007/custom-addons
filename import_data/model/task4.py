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

class country_code(models.Model):
    _inherit = 'res.country'

    # def name_get(self, cr, uid, ids, context):
    #     print "CONTEXT===============\n",context
    #     result = []
    #     if context.get('c_id',False):
    #         for each in self.browse(cr, uid , ids , context):
    #             print "IF=============\n",each
    #             result.append((each.id, each.name))
    #     else :
    #         for each in self.browse(cr, uid , ids , context):
    #             print "ELSE=============\n",each
    #             result.append((each.id, each.code))
    #     return result

    def name_search(self, cr, uid, name, args, operator, context, limit):
        print "CONTEXT SEARCH====================="
        result = []
        a = self.pool.get('res.country').browse(cr, uid, uid, context)
        print "a===============",a
        if context.get('c_id',False):
            for each in a:
                print "IF=============\n",each
                result.append((each.id, each.name))
        else :
            for each in a:
                print "ELSE=============\n",each
                result.append((each.id, each.code))
        return result





    # counter_field = fields.Integer('Counter Field:',default='0')
    # counter_field2 = fields.Integer('Counter Field2:')
    # counter_field3 = fields.Integer('Counter Field3:')
    #
    # # counter = 0
    # # counter1 = 0
    #
    # @api.multi
    # def name_get(self):
    #     print "=================COUNTRY CALLED============================="
    #     result = []
    #     for each in self:
    #         if each.counter_field == 0 and each.counter_field2 == 1 and each.counter_field3 == 0:
    #             new_name = str(each.code)
    #             result.append((each.id, new_name))
    #             print "IF 1==============",each.counter_field
    #             print "IF 2==============",each.counter_field2
    #             each.counter_field2 = 0
    #             each.counter_field3 = 1
    #         elif each.counter_field == 0 and each.counter_field2 == 0 and each.counter_field3 == 0:
    #             name = str(each.name)
    #             result.append((each.id, name))
    #             print "ELIF 1 1==============",each.counter_field
    #             print "ELIF 1 2==============",each.counter_field2
    #         elif each.counter_field == 0 and each.counter_field2 == 0 and each.counter_field3 == 1:
    #             # REFRESH CODE
    #             print "ELIF 2 1==================",each.counter_field
    #             print "ELIF 2 2==================",each.counter_field2
    #             new_name = str(each.code)
    #             result.append((each.id, new_name))
    #         each.counter_field = 0
    #     return result

        # self.counter1 += 1
        # elif self.counter1 > 0:
        #     print "COUNTER1=====================",self.counter1
        #     for each in self:
        #         new_name = str(each.code)
        #         result.append((each.id, new_name))
        #         country_code.counter = 0

  # elif each.counter_field == 0 and each.counter_field2 == 0 and each.counter_field3 == 1:
  #               print "ELIF 2 1==================",each.counter_field
  #               print "ELIF 2 2==================",each.counter_field2
  #               new_name = str(each.code)
  #               result.append((each.id, new_name))
  #               each.counter_field3 = 0
  # elif each.counter_field == 0 and each.counter_field2 == 1 and each.counter_field3 == 1:
  #               name = str(each.name)
  #               result.append((each.id, name))
  #               print "ELIF 3 1==================",each.counter_field
  #               print "ELIF 3 2==================",each.counter_field2



class res_partner_inherit(models.Model):
    _inherit = 'res.partner'


    @api.multi
    def write(self,vals):
        print "WRITE CALLDED======================"
        print "SELF CALLDED======================",self.id
        number = vals['country_id']
        record = self.env['res.country'].browse(vals['country_id'])
        vals.update({'country_id':number,'counter_field':1})
        self.env.cr.execute('update res_country set counter_field2 = %s where id = %s'%(1,number))
        print "VALS=======================",vals
        # country_code.counter += 1
        return super(res_partner_inherit, self).write(vals)

    @api.multi
    def custom_function(self):
        x = 100000
        print "CUSTOM PRIMNTING===================="
        return x


class inherit_sale_order(models.Model):
    _inherit = 'sale.order'

    extra_field = fields.Text('Text:')

    # @api.multi
    # def name_get(self,context='context'):
    #     print "INSIDE NAME GET=================="
    #     for record in self:
    #         print "RECORD===================",record
    #         print "SELF================",self
    #         print "CONTEXT FIRST================",self._context
    #         context = self._context.copy()
    #         if self._context.get('my_value') == True:
    #             context.update({'my_value':False})
    #         else :
    #             context.update({'my_value':True})
    #         print "CONTEXT LAST========================",context
    #         print "SELF CONTEXT========================",self._context
    #     return super(inherit_sale_order, self).name_get()


    # @api.multi
    # def function_name(self):
    #     print "SELF====================",self
    #     print "CONTEXT===================",self._context
    #     context = self._context.copy()
    #     context.update({'my_value':False})
    #     print "CONTEXT========================",context
    #     print "SELF CONTEXT========================",self._context


class sale_order_task(models.Model):
    _name = 'sale.order.task'

    order_name = fields.Char('Name:')
    order_amount = fields.Char('Amount:')

    @api.multi
    def get_details(self):
        print "DETAILS======================"
        self.env.cr.execute('delete from sale_order_task')
        list = []

        self.env.cr.execute('select so.name,so.amount_total from sale_order_line as sl LEFT JOIN sale_order as so ON sl.order_id = so.id WHERE so.amount_total > 2000 GROUP BY so.name,so.amount_total HAVING count(sl.order_id) > 2')
        record = self.env.cr.dictfetchall()
        print "RECORD===================================",record

        for each in record:
            list.append(each['name'])
            print "LIST-=================",list
        for each in record:
            print "EACH=====================",each
            self.create({'order_name':each['name'],'order_amount':each['amount_total']})


        return {'name': _("Warranty Claim Status"),
                'view_mode': 'tree,form',
                'res_id': False,
                'view_type': 'form',
                'res_model': 'sale.order',
                'type': 'ir.actions.act_window',
                'nodestroy': False,
                'view_id': False,
                'target': 'current',
                'domain':"[('name','in',%s)]" % list,
                }

