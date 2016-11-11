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


class alumni(models.Model):
    _name = 'alumni'
    _inherits = {'student':'choose_teachers'}



    choose_teachers = fields.Many2one('student','Choose Students: ')
    passout_year = fields.Selection([('1990',1990),('1991',1991),('1992',1992)],'PassOut :')
    second_name = fields.Char('Your Last Name Please:')




# class alumni_inherit(models.Model):
#     _inherit = 'student'
#
#     alumni_id = fields.Many2one('student','Alumni Id:')
