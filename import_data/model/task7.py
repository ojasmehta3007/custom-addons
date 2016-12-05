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
from openerp.addons.report_xlsx.report.report_xlsx import ReportXlsx
from cStringIO import StringIO

from openerp.report.report_sxw import report_sxw
from openerp.api import Environment

class purchase_order_custom(models.TransientModel):
    _name = 'purchase.order.custom'

    local = fields.Char('Local')

    @api.multi
    def transfer_order(self):
        print "TRANSFER ORDER========================="
        act_ids = self._context.get('active_ids')
        print "ACT IDS=======================",act_ids
        record = self.env['purchase.order'].browse(act_ids)
        id_list = []
        for each in record:
            print "RECORD=======================",each
            print "RECORD PARTNER_ID============",each.partner_id
            print "RECORD PAYMENT_ID============",each.payment_term_id
            key = str(each.partner_id) + str(each.payment_term_id)
            print "key====================",key

    # @api.multi
    # def transfer_order_new(self,next_rec,my_main,my_list,sub):
    #     name_list = ''
    #     name_source_write = self.env['purchase.order'].browse(my_main)
    #     for iter_list in my_list:
    #         rec_browse = self.env['purchase.order'].browse(iter_list)
    #                     # updating state
    #         if iter_list != my_main:
    #             rec_browse.update({'state':'cancel'})
    #             origin_name = rec_browse.name
    #             name_list += (str(origin_name) + ' , ')
    #                      # updating source document
    #         name_source_write.update({'origin':name_list})
    #                     # updating purchase order line
    #         line_record = self.env['purchase.order.line'].search([('order_id','=',iter_list)])
    #         for sub_line in line_record:
    #             if iter_list != my_main:
    #                 copy_line = sub_line.copy()
    #                 copy_line.update({'order_id':my_main})
    #
    # @api.multi
    # def transfer_order(self):
    #     record = self._context.get('active_ids')
    #     my_main = 0
    #     my_list = []
    #
    #     for each in record:
    #         rec = self.env['purchase.order'].browse(each)
    #         print "REC=============",rec
    #         name_id = rec.partner_id.id
    #         payment_id = rec.payment_term_id.id
    #         self.env.cr.execute("select partner_id,payment_term_id from purchase_order where partner_id = '%s' and payment_term_id = '%s' and id = '%s' " %(name_id,payment_id,each))
    #         next_rec = self.env.cr.fetchall()
    #         if next_rec not in my_list:
    #             my_list.append(rec.id)
    #         my_main = my_list[-1]
    #         sub = my_list[:-1]
    #         self.transfer_order_new(next_rec,my_main,my_list,sub)

    @api.model
    def default_get(self, fields):
         res = super(purchase_order_custom, self).default_get(fields)
         active_ids=self._context.get('active_ids')
         dict_compair={}
         sub_string=""
         for each in active_ids:
            print "EACH========================",each
            order_records=self.env["purchase.order"].browse(each)
            print "ORDER RECORDS=====================",order_records
            x= order_records.payment_term_id
            print "X===================\n",x
            if order_records.state=='cancel':
                print "INSIDE CANCEL====================="
                sub_string+=order_records.name+" , "
            key=str(order_records.partner_id)+str(order_records.payment_term_id)
            print "KEY==========================\n",key
            if dict_compair.get(key,False):
                ap=dict_compair.get(key)
                print "INSIDE IF BLOCK=================="
                print "AP=========================",ap
                print "APPEND AP=======================",ap.append(each)
                print "DICT UPDATE==========================\n",dict_compair.update({key:ap})
            else:
                print "INSIDE ELSE LOOP==================="
                ap=[]
                print "APPEND AP==========================",ap.append(order_records.id)
                print "DICT UPDATE========================",dict_compair.update({key:ap})
                print "DICT COMPAIR=========================\n",dict_compair.get(key)
         if sub_string!="":
             raise osv.except_osv('Warning!', "%s in cancel state"%(sub_string))
         for each in dict_compair.iterkeys():
             print "INSIDE FOR LOOP============================="
             first_value=[]
             add_purchase=dict_compair.get(each,False)
             print "ADD PURCHASE=========================",add_purchase
             if len(add_purchase)>1:
                 first_value=add_purchase[0]
                 print "FIRST VALUE=====================",first_value
                 ref_string=""
                 for id_list in add_purchase:
                    print "ID LIST=========================",id_list
                    if first_value!=id_list:
                        print "LAST BLOCK================================"
                        order_record=self.env["purchase.order"].browse(id_list)
                        ref_string+=order_record.name+"/"
                        order_record.update({'state':'cancel'})
                        x=order_record.order_line.copy()
                        for purchase_o_line in x:
                            purchase_o_line.update({'order_id':first_value})
         f_r=self.env["purchase.order"].browse(first_value)
         f_r.ref_order=ref_string
         print "REF ORDER===============================\n\n",f_r.ref_order
         return res

class taskincentory_custom(models.TransientModel):
    _name = 'taskinventory.custom'

    local = fields.Char('Local')

    @api.multi
    def bulktransfer(self):
        act_ids = self._context.get('active_ids')
        for each in act_ids:
            record = self.env['stock.picking'].browse(each)
            if record.state == 'assigned':
                trans = record.do_new_transfer()
                new_trans = self.env['stock.immediate.transfer'].search([('pick_id','=',record.id)])
                for my in new_trans:
                    my.process()



