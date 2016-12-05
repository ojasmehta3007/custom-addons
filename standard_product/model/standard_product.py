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

# class standard_product(models.Model):
#     _name = 'standard.product'

from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT

class sale_order_line_standard_product(models.Model):
    _inherit = 'sale.order'

    models_name = fields.Many2one('product.product','Select Your Product:')
    seq = 1

    @api.multi
    def apply_standard(self):
        my_list = []
        x = self.env['product.product'].browse(self.models_name.id)
        sale_create = self.env['sale.order.line'].create({'order_id':self.id,'product_uom':x.product_tmpl_id.uom_id.id,'name':self.models_name.name,'product_id':x.product_tmpl_id.id,'my_bool':False})
        counter_var = self.env['sale.order.line'].search([('order_id','=',self.id)])
        for each in counter_var:
            if each.my_bool == False:
                my_list.append(each.id)
                each.update({'sequence_no': self.seq})
                self.seq += 1
            else:
                print "INSIDE ELSE======================"

        date_field = datetime.strptime('1990-01-01 00:00:00', DEFAULT_SERVER_DATETIME_FORMAT)
        tmpl_id = x.product_tmpl_id.id
        bom_rec = self.env['mrp.bom'].search([('product_tmpl_id','=',tmpl_id)])
        bom_list = []
        for each in bom_rec:
            if date_field < datetime.strptime(each.write_date,DEFAULT_SERVER_DATETIME_FORMAT):
                date_field = datetime.strptime(each.write_date,DEFAULT_SERVER_DATETIME_FORMAT)
                bom_list.append(each.id)

        if bom_list == []:
            print "INSIDE EMPTY===================="
        else:
            latest = bom_list[-1]
            bom_line_rec = self.env['mrp.bom.line'].search(['&',('bom_id','=',latest),('standard','=',True)])
            for line in bom_line_rec:
                line_id = self.env['product.product'].search([('name_template','=',line.product_id.name_template)])
                self.env['sale.order.line'].create({'order_id':self.id,'product_uom':1,'name':line.product_id.name_template,'product_id':line_id.product_tmpl_id.id,'sale_order_child':sale_create.id})

        for each in my_list:
            rec = self.env['sale.order.line'].browse(each)
            next_rec = rec.sequence_no
            record = self.env['sale.order.line'].search([('sale_order_child','=',each)])
            for sequence in record:
                sequence.update({'sequence_no':next_rec})

class sale_order_line_standard(models.Model):
    _inherit = 'sale.order.line'

    sequence_no = fields.Integer('Sequence',default=0)
    my_bool = fields.Boolean('Boolean',default=True)
    sale_order_child = fields.Many2one('sale.order.line')

    @api.multi
    def unlink(self):
        if not self.sale_order_child :
            record = self.env['sale.order.line'].search([('sale_order_child','=',self.id)])
            for each in record:
                each.unlink()
            self.reorder()
        return super(sale_order_line_standard, self).unlink()

    @api.model
    def reorder(self):
        seq = 1
        order = self.order_id.id
        record = self.env['sale.order.line'].search([('order_id','=',order)])
        for each in record:
            if each.id == self.id :
                continue
            else:
                if each.my_bool == False:
                    each.update({'sequence_no':seq})
                    seq = seq + 1
                else:
                    each.update({'sequence_no':seq})

class mrp_standard_product(models.Model):
    _inherit = 'mrp.bom.line'

    standard = fields.Boolean('Standard')

 # FOR PARENT SEQUENCE UPDATION
        # if len(counter_var) == 1:
        #     for each in counter_var:
        #         local = each.sequence_no + 1
        #         counter_var.update({'sequence_no':local})
        # elif len(counter_var) > 1:
        #     for each in counter_var:
        #         my_list.append(each.id)
        #     var1 = my_list[-1]
        #     var2 = my_list[-2]
        #     back = self.env['sale.order.line'].browse(var2)
        #     if back.sequence_no == 0:
        #         self.env.cr.execute("select * from sale_order_line where order_id = '%d' and my_bool = 'f'" %(self.id))
        #         record = self.env.cr.dictfetchall()[0]
                # new_var = record.get('id')
                # new_back = self.env['sale.order.line'].browse(new_var)
                # new_back.update({'sequence_no':local})
            # else:
            #     # new_back = self.env['sale.order.line'].update({'sequence_no':local})
            #     local = back.sequence_no
            #     local = local + 1
            #     new_back = self.env['sale.order.line'].browse(var1)
            #     new_back.update({'sequence_no':local})


                        # FOR ONLY PARENT UPDATION
        # for i in range (0,len(counter_var)):
        #     local_var = counter_var[i].id
        #     self.env.cr.execute("select id from sale_order_line where id = %d and my_bool = 'f' " %(local_var))
        #     record = self.env.cr.dictfetchall()[0]
        #     var = record.get('id')
        #     rec = self.env['sale.order.line'].browse(var)
        #     rec.update({'sequence_no':i+1})
