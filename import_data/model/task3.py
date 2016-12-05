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

class task3(models.Model):
    _name = 'task3'

    name = fields.Char('Name:')
    roll_no = fields.Integer('Roll No:')
    partner = fields.Many2one('res.partner','select Partner:')
    stand = fields.Integer('Standard:',default='3',readonly=True)

    @api.model
    def create(self,vals,context):
        print "INSIDE CREATE==============="
        print "SELF=================",self._context
        print "VALS=================",vals
        print "VALS=================",vals['name']
        print "VALS=================",vals['roll_no']
        d_name = vals['name']
        d_roll_no = vals['roll_no']

        vals = {
            'd_name':d_name,
            'd_roll_no':d_roll_no,
        }
        # for record in self.env['demo.class']
        # res = self.env['demo.class'].create(vals)
        return super(task3, self).create(vals)

class demo_class(models.Model):
    _name = 'demo.class'

    get_details = fields.One2many('task3','partner','Details:')
    d_name = fields.Char('Name:')
    d_roll_no = fields.Integer('Roll No:')

