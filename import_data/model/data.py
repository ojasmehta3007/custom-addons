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

class import_data(models.Model):
    _name = 'import.data'

    binary_data = fields.Binary('Binary Field')

    # @api.multi
    # def create_custom(self,local):
    #
    #     self.env['product.template'].sudo().create({'name':local[0]})
    #     self.env.cr.execute("SELECT id from product_template where name = '%s'" %(local[0]))
    #     vals = self.env.cr.fetchone()[0]
    #     vals1 = self.env['product.template'].browse(vals)
    #
    #     self.env.cr.execute("SELECT id from product_category where name = '%s'" % (local[2]))
    #     prod_catg1 = self.env.cr.fetchone()[0]
    #
    #     bool = True
    #     purch = True
    #     c = ''
    #     act = True
    #     pcm = ''
    #     pv = ''
    #     routes_buy1 = 0
    #
    #     if local[3] == 'Y': bool = True
    #     elif local[3] == 'N': bool = False
    #     if local[4] == 'Y': purch = True
    #     elif local[4] == 'N': purch = False
    #     if local[5] == 'Consumable' or local[5] == 'consumable' : c = 'consu'
    #     elif local[5] == 'Stockable Product' or local[5] == 'stockable product': c = 'product'
    #     elif local[5] == 'service' or local[5] == 'Service': c = 'service'
    #     if local[6] == 'Y' or local[6] == 'y' : act = True
    #     elif local[6] == 'N' or local[6] == 'n': act = False
    #
    #
    #     if local[8] == 'Standard Price' or local[8] == 'standard price': pcm = 'standard'
    #     elif local[8] == 'Average Price' or local[8] == 'average price': pcm = 'average'
    #     elif local[8] == 'Real Price' or local[8] == 'real price': pcm = 'real'
    #     if local[10] == 'Buy' or local[10] == 'buy':
    #         self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
    #         routes_buy1 = self.env.cr.fetchone()[0]
    #     elif local[10] == 'Make To Order' or local[10] == 'make to order' or local[10] == 'Make to Order':
    #         self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
    #         routes_buy1 = self.env.cr.fetchone()[0]
    #     elif local[10] == 'Manufacture' or local[10] == 'manufacture':
    #         self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
    #         routes_buy1 = self.env.cr.fetchone()[0]
    #     if local[11] == 'Periodic(manual)' or local[11] == 'periodic(manual)':
    #         pv = 'manual_periodic'
    #     elif local[11] == 'Perpetual(automated)' or local[11] == 'perpetual(automated)':
    #         pv = 'real_time'
    #     self.env.cr.execute("SELECT id from account_account where name = '%s' " %(local[12]))
    #     record1 = self.env.cr.fetchone()[0]
    #     self.env.cr.execute("SELECT id from account_account where name ='%s'" %(local[13]))
    #     account_record1 = self.env.cr.fetchone()[0]
    #     self.env.cr.execute("SELECT id from account_account where name = '%s'" %(local[14]))
    #     stock_record_income1 = self.env.cr.fetchone()[0]
    #     self.env.cr.execute("SELECT id from account_account where name = '%s'" %(local[15]))
    #     stock_record_outcome1 = self.env.cr.fetchone()[0]
    #
    #
    #     vals1.sudo().write({'description':local[1],
    #                         'categ_id':prod_catg1,
    #                         'sale_ok':bool,
    #                         'purchase_ok':purch,
    #                         'type':c,
    #                         'active':act,
    #                         'default_code':local[7],
    #                         'property_cost_method':pcm,
    #                         'standard_price':local[9],
    #                         'route_ids':[(6,0,[routes_buy1])],
    #                         'property_valuation':pv,
    #                         'property_account_income_id':record1,
    #                         'property_account_expense_id':account_record1,
    #                         'property_stock_account_input':stock_record_income1,
    #                         'property_stock_account_output':stock_record_outcome1,
    #                         })
    # @api.multi
    # def update_custom(self,local,new_vals):
    #     sale = ''
    #     purchase = ''
    #     product_type = ''
    #     act = ''
    #     price = ''
    #     routes_buy1 = 0
    #     property=''
    #     self.env.cr.execute("SELECT id from product_category where name = '%s'" %(local[2]))
    #     prod_catg1 = self.env.cr.fetchone()[0]
    #     if local[3] == 'Y': sale = True
    #     elif local[3] == 'N': sale = False
    #     if local[4] == 'Y': purchase = True
    #     elif local[5] == 'N': purchase = False
    #     if local[5] == 'Consumable' or local[5] == 'consumable' : product_type = 'consu'
    #     elif local[5] == 'Stockable Product' or local[5] == 'Stockable product': product_type = 'product'
    #     elif local[5] == 'service' or local[5] == 'Service': product_type = 'service'
    #     if local[6] == 'Y' or local[6] == 'y' : act = True
    #     elif local[6] == 'N' or local[6] == 'n': act = False
    #     if local[8] == 'Standard Price' or local[8] == 'standard price': price = 'standard'
    #     elif local[8] == 'Average Price' or local[8] == 'average price': price = 'average'
    #     elif local[8] == 'Real Price' or local[8] == 'real price': price = 'real'
    #     if local[10] == 'Buy' or local[10] == 'buy':
    #         self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
    #         routes_buy1 = self.env.cr.fetchone()[0]
    #     elif local[10] == 'Make To Order' or local[10] == 'make to order' or local[10] == 'Make to Order':
    #         self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
    #         routes_buy1 = self.env.cr.fetchone()[0]
    #     elif local[10] == 'Manufacture' or local[10] == 'manufacture':
    #         self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
    #         routes_buy1 = self.env.cr.fetchone()[0]
    #     if local[11] == 'Periodic(manual)' or local[11] == 'periodic(manual)': property = 'manual_periodic'
    #     elif local[11] == 'Perpetual(automated)' or local[11] == 'perpetual(automated)': property = 'real_time'
    #     self.env.cr.execute("SELECT id from account_account where name = '%s' " %(local[12]))
    #     record1 = self.env.cr.fetchone()[0]
    #     self.env.cr.execute("SELECT id from account_account where name ='%s'" %(local[13]))
    #     account_record1 = self.env.cr.fetchone()[0]
    #     self.env.cr.execute("SELECT id from account_account where name = '%s'" %(local[14]))
    #     stock_record_income1 = self.env.cr.fetchone()[0]
    #     self.env.cr.execute("SELECT id from account_account where name = '%s'" %(local[15]))
    #     stock_record_outcome1 = self.env.cr.fetchone()[0]
    #     new_vals.sudo().write({
    #         'description':local[1],
    #         'categ_id':prod_catg1,
    #         'sale_ok':sale,
    #         'purchase_ok':purchase,
    #         'type':product_type,
    #         'active':act,
    #         'default_code':local[7],
    #         'property_cost_method':price,
    #         'standard_price':local[9],
    #         'route_ids':[(6,0,[routes_buy1])],
    #         'property_valuation':property,
    #         'property_account_income_id':record1,
    #         'property_account_expense_id':account_record1,
    #         'property_stock_account_input':stock_record_income1,
    #         'property_stock_account_output':stock_record_outcome1,
    #     })

    @api.multi
    def mixed_function(self,local):
        print "INSIDE MIXED FUNCTION==============================\n"
        # sale = ''
        # purchase = ''
        # product_type = ''
        # act = ''
        # price = ''
        # routes_buy1 = 0
        # property=''
        #
        # self.env.cr.execute("SELECT id from product_category where name = '%s'" %(local[2]))
        # prod_catg1 = self.env.cr.fetchone()[0]
        #
        # if local[3] == 'Y': sale = True
        # elif local[3] == 'N': sale = False
        #
        # if local[4] == 'Y': purchase = True
        # elif local[5] == 'N': purchase = False
        #
        # if local[5] == 'Consumable' or local[5] == 'consumable' : product_type = 'consu'
        # elif local[5] == 'Stockable Product' or local[5] == 'stockable product': product_type = 'product'
        # elif local[5] == 'service' or local[5] == 'Service': product_type = 'service'
        #
        # if local[6] == 'Y' or local[6] == 'y' : act = True
        # elif local[6] == 'N' or local[6] == 'n': act = False
        #
        # if local[8] == 'Standard Price' or local[8] == 'standard price': price = 'standard'
        # elif local[8] == 'Average Price' or local[8] == 'average price': price = 'average'
        # elif local[8] == 'Real Price' or local[8] == 'real price': price = 'real'
        #
        # if local[10] == 'Buy' or local[10] == 'buy':
        #     self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
        #     routes_buy1 = self.env.cr.fetchone()[0]
        # elif local[10] == 'Make To Order' or local[10] == 'make to order' or local[10] == 'Make to Order':
        #     self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
        #     routes_buy1 = self.env.cr.fetchone()[0]
        # elif local[10] == 'Manufacture' or local[10] == 'manufacture':
        #     self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
        #     routes_buy1 = self.env.cr.fetchone()[0]
        #
        # if local[11] == 'Periodic(manual)' or local[11] == 'periodic(manual)': property = 'manual_periodic'
        # elif local[11] == 'Perpetual(automated)' or local[11] == 'perpetual(automated)': property = 'real_time'
        #
        # self.env.cr.execute("SELECT id from account_account where name = '%s' " %(local[12]))
        # record1 = self.env.cr.fetchone()[0]
        #
        # self.env.cr.execute("SELECT id from account_account where name ='%s'" %(local[13]))
        # account_record1 = self.env.cr.fetchone()[0]
        #
        # self.env.cr.execute("SELECT id from account_account where name = '%s'" %(local[14]))
        # stock_record_income1 = self.env.cr.fetchone()[0]
        #
        # self.env.cr.execute("SELECT id from account_account where name = '%s'" %(local[15]))
        # stock_record_outcome1 = self.env.cr.fetchone()[0]


        new_vals = self.env['product.template'].search([('name','=',local[0])])
        if new_vals.name == local[0]:
            print "Inside UPDATE===========================\n",
            # new_vals.sudo().write({
            #                         'description':local[1],
            #                         'categ_id':prod_catg1,
            #                         'sale_ok':sale,
            #                         'purchase_ok':purchase,
            #                         'type':product_type,
            #                         'active':act,
            #                         'default_code':local[7],
            #                         'property_cost_method':price,
            #                         'standard_price':local[9],
            #                         'route_ids':[(6,0,[routes_buy1])],
            #                         'property_valuation':property,
            #                         'property_account_income_id':record1,
            #                         'property_account_expense_id':account_record1,
            #                         'property_stock_account_input':stock_record_income1,
            #                         'property_stock_account_output':stock_record_outcome1,
            #                      })

        elif new_vals.name != local[0]:
            print "INSIDE CREATE================================\n"
            self.env['product.template'].sudo().create({'name':local[0]})
            self.env.cr.execute("SELECT id from product_template where name = '%s'" %(local[0]))
            vals = self.env.cr.fetchone()[0]
            vals1 = self.env['product.template'].browse(vals)
            # vals1.sudo().write({
            #                         'description':local[1],
            #                         'categ_id':prod_catg1,
            #                         'sale_ok':sale,
            #                         'purchase_ok':purchase,
            #                         'type':product_type,
            #                         'active':act,
            #                         'default_code':local[7],
            #                         'property_cost_method':price,
            #                         'standard_price':local[9],
            #                         'route_ids':[(6,0,[routes_buy1])],
            #                         'property_valuation':property,
            #                         'property_account_income_id':record1,
            #                         'property_account_expense_id':account_record1,
            #                         'property_stock_account_input':stock_record_income1,
            #                         'property_stock_account_output':stock_record_outcome1,
            #                      })



    @api.multi
    def variables(self,local):
        # list.append(9)
        print "INSIDE VARIABLES==============================\n"
        sale = ''
        purchase = ''
        product_type = ''
        act = ''
        price = ''
        routes_buy1 = 0
        property=''

        self.env.cr.execute("SELECT id from product_category where name = '%s'" %(local[2]))
        prod_catg1 = self.env.cr.fetchone()[0]

        if local[3] == 'Y': sale = True
        elif local[3] == 'N': sale = False

        if local[4] == 'Y': purchase = True
        elif local[5] == 'N': purchase = False

        if local[5] == 'Consumable' or local[5] == 'consumable' : product_type = 'consu'
        elif local[5] == 'Stockable Product' or local[5] == 'stockable product': product_type = 'product'
        elif local[5] == 'service' or local[5] == 'Service': product_type = 'service'

        if local[6] == 'Y' or local[6] == 'y' : act = True
        elif local[6] == 'N' or local[6] == 'n': act = False

        if local[8] == 'Standard Price' or local[8] == 'standard price': price = 'standard'
        elif local[8] == 'Average Price' or local[8] == 'average price': price = 'average'
        elif local[8] == 'Real Price' or local[8] == 'real price': price = 'real'

        if local[10] == 'Buy' or local[10] == 'buy':
            self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
            routes_buy1 = self.env.cr.fetchone()[0]
        elif local[10] == 'Make To Order' or local[10] == 'make to order' or local[10] == 'Make to Order':
            self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
            routes_buy1 = self.env.cr.fetchone()[0]
        elif local[10] == 'Manufacture' or local[10] == 'manufacture':
            self.env.cr.execute("select id from stock_location_route where name = '%s'" %local[10])
            routes_buy1 = self.env.cr.fetchone()[0]

        if local[11] == 'Periodic(manual)' or local[11] == 'periodic(manual)': property = 'manual_periodic'
        elif local[11] == 'Perpetual(automated)' or local[11] == 'perpetual(automated)': property = 'real_time'

        self.env.cr.execute("SELECT id from account_account where name = '%s' " %(local[12]))
        record1 = self.env.cr.fetchone()[0]

        self.env.cr.execute("SELECT id from account_account where name ='%s'" %(local[13]))
        account_record1 = self.env.cr.fetchone()[0]

        self.env.cr.execute("SELECT id from account_account where name = '%s'" %(local[14]))
        stock_record_income1 = self.env.cr.fetchone()[0]

        self.env.cr.execute("SELECT id from account_account where name = '%s'" %(local[15]))
        stock_record_outcome1 = self.env.cr.fetchone()[0]

        new_list = [prod_catg1,sale,purchase,product_type,act,price,routes_buy1,property,record1,account_record1,stock_record_income1,stock_record_outcome1]
        print "NEW LIST RECORDS======================================",new_list
        return new_list


    @api.multi
    def import_data_calculate(self):
        print "Start",datetime.now()
        data = self.binary_data
        file_datas = base64.b64decode(data)
        file = open("/home/bista/odoo-9/new_file.xls", "w")
        file.write(file_datas)
        file.close()
        book = xlrd.open_workbook("/home/bista/odoo-9/new_file.xls")
        first_sheet = book.sheet_by_index(0)
        n = 2
        for i in range(2,first_sheet.nrows):
            print "NUMBER=======================\n",i
            local = first_sheet.row_values(n,0)
            # list = [1,2,3,4,5]
            if i == n:
                y=self.variables(local)
                print "==================\n",y

            self.mixed_function(local)
            print "OUTSIDE FUNCTION==================",y

            # new_vals = self.env['product.template'].search([('name','=',local[0])])



            # if new_vals.name == local[0]:
            #     self.update_custom(local,new_vals)
            # elif new_vals.name != local[0]:
            #     self.create_custom(local)
            n = n+1
        print "Stop",datetime.now()







