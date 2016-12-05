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


class sale_order_inherit(models.Model):
    _name = 'sale.order.inherit'
    # _description = "Sales Orders Statistics"
    _auto = False
    # _rec_name = 'date'

    my_name = fields.Many2one('product.product','NAME:')
    my_total_qty = fields.Integer('TOTAL QTY:')
    my_price_unit = fields.Integer('PRICE UNIT')
    my_price_total = fields.Integer('PRICE TOTAL')
    my_avg_unit_price = fields.Integer('AVERAGE PRICE')
    default_code = fields.Char('DEFAULT CODE:')

    # def _select(self):
    #     print "INSIDE SELECT============================="
    #     select_str = """select distinct product_id as my_name,min(id) as id,
    #     SUM(product_uom_qty) as my_total_qty,
    #     SUM(price_unit) as my_price_unit,
    #     SUM(product_uom_qty * price_unit) as my_price_total,
    #     (SUM(product_uom_qty * price_unit) / SUM(product_uom_qty)) AS my_avg_unit_price"""
    #     return select_str

    def _select(self):
        print "INSIDE SELECT============================="
        select_str = """SELECT distinct sl.product_id as my_name,min(sl.id) as id,
        SUM(sl.product_uom_qty) as my_total_qty,
        SUM(sl.price_unit) as my_price_unit,
        SUM(product_uom_qty * price_unit) as my_price_total,
        SUM(sl.product_uom_qty * sl.price_unit) / SUM(sl.product_uom_qty) AS my_avg_unit_price,
        pp.default_code as default_code"""
        return select_str


    def _from(self):
        print "INSIDE FROM=========================="
        from_str = """sale_order_line sl LEFT JOIN product_product pp ON sl.product_id = pp.id"""
        return from_str

    def _group_by(self):
        group_by_str = """GROUP BY sl.product_id,pp.default_code ORDER BY sl.product_id DESC"""
        return group_by_str

    # def _order_by(self):
    #     order_by_str = """"""
    #     return order_by_str

    def init(self, cr):
        print "INSIDE INIT==========================="
        # self._table = sale_report
        tools.drop_view_if_exists(cr, self._table)
        cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            FROM %s
            %s
            )""" % (self._table, self._select(), self._from(),self._group_by()))


