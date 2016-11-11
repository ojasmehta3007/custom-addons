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
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8
from openerp.exceptions import except_orm,UserError, ValidationError

import re
import time
import datetime
from datetime import datetime
from time import gmtime, strftime


class employee(models.Model):
    _inherit = 'hr.employee'


    state = fields.Selection([('new', 'NEW') , ('probation', 'PROBATION') , ('confirmed','CONFIRMED') , ('terminated','TERMINATED') , ('resigned','RESIGNED')], 'Status:')
    # ([('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four')], 'Stand.')

    @api.model
    def create(self,vals):
        list = ['@','.']
        if vals.get('work_email',False):
            email = vals.get('work_email',False)
            print "EMAIL=========================",vals
            print "EMAIL email=========================",email
            for each in list:
                if email.count('@') > 1:
                    raise except_orm(_("Use Only one @" ))
                if email.count('.') > 4:
                    raise except_orm(_('Don\'t use . unnecessarily'))
                a = email.find('@')
                print "a===================",a
                b = email.find('.')
                print "b===================",b

    @api.multi
    def write(self, vals):
        list = ['@','.']
        if vals.get('work_email',False):
            email = vals.get('work_email',False)
            print "EMAIL=========================",vals
            print "EMAIL email=========================",email
            length_email = len(email)
            print "LENGTH OF EMAIL============",length_email
            at_the_rate = email.find('@')
            print "Finding @ ===================",at_the_rate
            full_stop = email.find('.')
            print "FINDING first point======================",full_stop
            r_full_stop = email.rfind('.')
            print "reverse point=================",r_full_stop
            for my in range(at_the_rate , r_full_stop):
                print "my=======================",my
            for each in list:
                if email.count('@') > 1:
                    raise except_orm(_("Use Only one @" ))
                # if email.count('.') > 3:
                #     raise except_orm(_('Don\'t use . unnecessarily'))
                for my in range(at_the_rate+1 , r_full_stop):
                    print "my=======================",email[my]
                    if email[my].isalpha():
                        pass
                    else:
                        raise except_orm(_("Waring...."))
            return super(employee,self).write(vals)







                
class sale_inherit(models.Model):
    _inherit = 'sale.order'
    



    def calculate_weight(self):
        weight = 0
        for each in self.order_line:
            print "EACH======================",each
            weight = weight + each.product_id.weight * each.product_uom_qty
            print "WEIGHT=========================",weight
        self.total_weight = weight


    is_required = fields.Boolean('Is_Required')
    total_weight = fields.Char('Total Weight',compute='calculate_weight')


    @api.multi
    @api.onchange('partner_id')
    def myfucntion(self):
        a = self.partner_id
        print "a========",a.id

        # b = self.env['res.partner'].browse(a)
        # print "b=====================",b
        # print "Company TYPE=======================",b.company_type
        if a.company_type == 'company':
            print "COMPANY TYPE=============",a.company_type
            self.is_required = True
        else:
            self.is_required = False



    @api.multi
    def unlink(self):
        if self.amount_total > 10000:
            raise except_orm(_("Warning....You Can't Delete This Record"))
        else:
            pass
        return super(sale_inherit, self).unlink()

class sale_order_custom(models.TransientModel):
    _name = 'sale.order.cust'

    product = fields.Many2one('product.product','Product:')
    qty = fields.Integer('Quantity:')
    unit_price = fields.Integer('Unit Price:')

    @api.multi
    def insert_wiz(self,vals):
        print "vals=================",vals
        product_name = self.product
        print "a=================",product_name
        product_qty = self.qty
        print "qty==============",product_qty
        units = self.unit_price
        print "units==================",units
        # active_id = self._context.get('active_id')
        my_id = vals.get('active_id')
        print "=========================================",my_id
        # print "activeID=====",active_id
        a = self.env['sale.order.line'].create({'product_id':product_name.id,'product_uom_qty':product_qty,'price_unit':units,'order_id':my_id})
        print "a========================",a


class sale_order_line_cust(models.Model):
    _inherit = 'sale.order.line'


    product_type = fields.Selection('Product_type',related='product_id.type')

    # @api.onchange('product')
    # def change_product(self):
    #     product_id = self.product_id.id
    #     print "Product ID=================",product_id
    #     a = self.env['product.product'].browse(product_id)
    #     print "a=======",a
    #     b = a.product_tmpl_id.id
    #     print "b==================",b
    #     c = self.env['product.template'].browse(b)
    #     print "TYPE===================",c.type
    #     self.product_type = c.type






class purchase_order_custom(models.Model):
    _inherit = 'purchase.order.line'

    product_type = fields.Char('Product Type')

    @api.onchange('product_id')
    def change_product(self):
        print "SELF product ID==============================",self.product_id
        print "SELF product TMPL ID==============================",self.product_id.product_tmpl_id
        print "SELF type==============================",self.product_id.product_tmpl_id.type

        self.product_type = self.product_id.product_tmpl_id.type

        # product_id = self.product_id.id
        # print "Product ID=================",product_id
        # a = self.env['product.product'].browse(product_id)
        # print "a=======",a
        # b = a.product_tmpl_id.id
        # print "b==================",b
        # c = self.env['product.template'].browse(b)
        # self.product_type = c.type
