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

class subjects(models.Model):
    _name = 'subject'
    _rec_name = 'subject'

    select_student = fields.Many2one('student','Select Student:')
    subject = fields.Char('Title : ')
    subject1 = fields.Integer('Physics: ')
    subject2 = fields.Integer('Chemistry: ')
    subject3 = fields.Integer('Maths: ')
    percentage = fields.Float('Percentage:')
    choose_teacher = fields.Many2one('teacher','Choose Teacher :')

    teacher_expense = fields.Integer('Teacher fees Expected: ')
    tution_fees = fields.Integer('Tution Fees :')
    travel_expense = fields.Integer('Travel Expense: ')

    @api.multi
    @api.onchange('teacher_expense')
    def calculation(self):
        self.tution_fees = self.teacher_expense + 2000
        self.travel_expense = self.tution_fees - 1000



    @api.multi
    @api.onchange('percentage','subject1','subject2','subject3')
    def calculate(self):
        total = 300
        total_marks = self.subject1 + self.subject2 + self.subject3
        self.percentage = (total_marks * 100) / total




