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

class marks_child(models.TransientModel):
    _name = 'marks.child'
    _rec_name = 'student_name_ref'

    marks_parent_M2O = fields.Many2one('marks','Marks Calling Child:')

    student_name_ref = fields.Many2one('student','Student Name Ref:')
    subject_name_ref = fields.Many2one('subject.details','Subject Name Ref:')
    marks_of_student = fields.Integer('Marks Of Student:')


    # details of marks

    # subject10 = fields.Integer('Physics:')
    # subject20 = fields.Integer('Chemistry')
    # subject30 = fields.Integer('Maths')
    # percentage_new = fields.Float('Percentage : ')
    # marks_parent_O2M = fields.One2many('marks','marks_child_M20','Marks_calling_child:')


