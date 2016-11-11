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

class employee_information(models.Model):
    _name = 'employee.information'

    emp_id = fields.Integer('Employee_ID', required=True)
    emp_name = fields.Char('Employee Name', required=True)
    city = fields.Char('City')
    pincode = fields.Integer('Pincode')
    #active = fields.Boolean('Active',  default=1)
    working_address = fields.Text('Working Address')
    work_email =  fields.Char('Work Email')
    work_phone = fields.Char('Work Phone')
    work_mobile = fields.Integer('Work Mobile')
    office_location = fields.Char('Office Location')
    company_code = fields.Char('Company Code')
    nationality = fields.Char('Nationality')
    education_level = fields.Char('Education Level')
    college_name = fields.Char('College Name')
    birth = fields.Date('Birth')
    date_of_birth = fields.Datetime('Date Of Birth' , required=True)




