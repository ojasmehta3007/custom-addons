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

class sale_order_line_custom(models.Model):
    _name = 'sale.order.line.custom'

    # local = fields.Char('Local')

    @api.multi
    def get_details(self):
        print "GET DETAILS======================"

        # self.env.cr.execute('drop table sale_order_line_custom')
        # print "DROPPED TABLE===================="
        # self.env.cr.execute('CREATE TABLE sale_order_line_custom(id,create_date,product_uom,sequence,price_unit,product_uom_qty,price_subtotal,write_uid,currency_id,create_uid,price_tax,qty_to_invoice,customer_lead,company_id,state,order_partner_id,order_id,qty_invoiced,discount,write_date,price_reduce,qty_delivered,price_total,invoice_status,name,salesman_id,product_id,product_packaging,route_id) AS SELECT * FROM sale_order_line')
        # record = self.env.cr.dictfetchall()
        # print "record===============================",record
        # self.env.cr.execute('INSERT INTO sale_order_line_custom AS SELECT * FROM sale_order_line')
        # record = self.env.cr.dictfetchall()
        # print "RECORD=================",record
        # # print "RECORD=================",record[0]
        # # print "RECORD=================",record[0].get('id',False)
        #
        # for each in record:
        #     print "EACH==================",each
        #     print "EACH==================",each.get('id',False)
        #     result.append(each.get('id'))
        #     print "RESULT===================",result


        return {'name': _("Sale Order Line"),
                'view_mode': 'tree,form',
                'res_id': False,
                'view_type': 'form',
                'res_model': 'sale.order.line',
                'type': 'ir.actions.act_window',
                'nodestroy': False,
                'view_id': False,
                'target': 'current',
                }

class PartnerXlsx(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, partners):

        print "Self=================",self
        print "Self=================",workbook
        report_name = "SHEET"
        n = 1
        # One sheet by partner
        sheet = workbook.add_worksheet(report_name[:31])
        sheet.freeze_panes(1, 1)
        myformat = workbook.add_format()
        myformat.set_fg_color('#00FFFF')
        myformat.set_bold()
        myformat.set_border(2)
        sheet.set_column(0, 8, 20)

        myformat1 = workbook.add_format()
        myformat1.set_fg_color('#FFF0FF')

        sheet.write(0, 0, "Order Referance", myformat)
        sheet.write(0, 1, "Customer", myformat)
        sheet.write(0, 2, "Description", myformat)
        sheet.write(0, 3, "Salesperson", myformat)
        sheet.write(0, 4, "Qty", myformat)
        sheet.write(0, 5, "Delivered", myformat)
        sheet.write(0, 6, "Invoiced", myformat)
        sheet.write(0, 7, "To Invoice", myformat)
        sheet.write(0, 8, "Subtotal", myformat)
        sheet.write(0, 9, "Unit Price", myformat)
        for obj in partners:
            sheet.write(n, 0, obj.order_id.name, myformat1)
            sheet.write(n, 1, obj.order_partner_id.name, myformat1)
            sheet.write(n, 2, obj.name, myformat1)
            sheet.write(n, 3, obj.salesman_id.name, myformat1)
            sheet.write(n, 4, obj.product_uom_qty, myformat1)
            sheet.write(n, 5, obj.qty_delivered, myformat1)
            sheet.write(n, 6, obj.qty_invoiced, myformat1)
            sheet.write(n, 7, obj.qty_to_invoice , myformat1)
            sheet.write(n, 8, obj.currency_id.symbol+ ' '+str(obj.price_subtotal), myformat1)
            sheet.write(n, 9, obj.currency_id.symbol+ ' '+str(obj.price_unit), myformat1)
            n = n+1

PartnerXlsx('report.res.partner.xlsx',
            'sale.order.line')

# class SaleOrderLineXlsx(ReportXlsx):
#
#     def generate_xlsx_report(self, workbook, data, sale_order_lines):
#         for obj in sale_order_lines:
#             report_name = obj.name
#             sheet = workbook.add_worksheet("sheet")
#             bold = workbook.add_format({'bold': True})
#             sheet.write(0, 0, obj.order_id, bold)
#
# SaleOrderLineXlsx('report.sale.order.line.xlsx','sale.order.line')
