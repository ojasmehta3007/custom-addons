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

class student_student(models.Model):
    _name = 'student.student'

    name = fields.Many2one('res.partner',string='Student Name:')
    roll_no = fields.Integer('Roll No:')
    total_amount = fields.Integer('Total Amount/Month:')
    is_true = fields.Boolean('is_true',default=True)
    total_amount_due = fields.Integer('Total Amount Due:',compute='calculate_amount_due_total',store=True)
    for_month = fields.Integer('For months:')
    standard = fields.Integer('Class:')
    sidd_challenge = fields.One2many('wizard.total.calculate.o2m','sidd_challenge_2','TRY :')

    @api.multi
    def pass_roll_no(self):
        print "SELF===================================",self._context
        roll_no_id = self.roll_no
        print "ROLL NO===============================",roll_no_id
        return{
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.fees.calculate',
            'view_mode': 'form',
            'view_type': 'form',
            'context' : {'default_roll_no':roll_no_id},
            'views': [(False, 'form')],
            'target': 'new',
        }

    @api.model
    def default_get(self, fields_list):
        print "DEFAULT GET==========================="
        res = super(student_student, self).default_get(fields_list)
        res.update({'total_amount':500})
        return res

    @api.multi
    @api.depends('sidd_challenge')
    def calculate_amount_due_total(self):
        print "Inside========================"
        print "============================",self.sidd_challenge
        total = 0

        for each in self.sidd_challenge:
            print "EACH=============================",each.amount_due
            total = total + each.amount_due
        self.total_amount_due = total

class wizard_class_fees_calculate(models.TransientModel):
    _name = 'wizard.fees.calculate'

    computer_fee = fields.Integer('Computer Fee:')
    tution_fee = fields.Integer('Tution Fee:')
    monthly_fee = fields.Integer('Monthly Fee:')
    month_name = fields.Char('Month Name:')
    date_time = fields.Date('Date:')
    roll_no = fields.Integer('Roll No:')

    @api.multi
    @api.onchange('date_time')
    def change_date(self):
        curr_date = self.date_time
        if curr_date == False:
            print "FALSE"
        else:
            curr_birth_date = datetime.strptime(str(curr_date),"%Y-%m-%d")
            m_num = curr_birth_date.month
            mon_name = calendar.month_name[m_num]
            self.month_name = mon_name


    @api.multi
    def pass_all_values(self):
        print "Compute Fee======================",self.computer_fee
        print "tution Fee======================",self.tution_fee
        print "monthly Fee======================",self.monthly_fee
        print "CONTEXT======================",self._context
        paid_fees = self.computer_fee + self.tution_fee + self.monthly_fee
        print "PAID FEES================",paid_fees
        total_amount = 500
        amount_due = total_amount - paid_fees
        print "AMOUNT DUE================================",amount_due
        active_id=self._context.get('active_id')
        print "ACTIVE ID===============================",active_id
        # self.env['wizard.total.calculate.o2m'].create({'month_name':self.month_name,"sidd_challenge_2":active_id})

        act=self.env['wizard.total.calculate'].create({"paid_fees":paid_fees,"amount_due":amount_due,"act":active_id,"my_month":self.month_name})
        return {
                        'name': 'NEw Wizard',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'wizard.total.calculate',
                        'res_id': act.id,
                        'type': 'ir.actions.act_window',
                        'views': [(False, 'form')],
                        'target': 'new',
            }

class wizard_total_calculation(models.TransientModel):
    _name = 'wizard.total.calculate'

    paid_fees = fields.Integer('Paid Fees:')
    amount_due = fields.Integer('Amount Due:')
    act=fields.Integer("id")
    my_month = fields.Char("Month")


    @api.multi
    def o2m_calculate(self):
        print "ACT============================================",self.act
        self.env['wizard.total.calculate.o2m'].create({"sidd_challenge_2":self.act,"paid_fees":self.paid_fees,"amount_due":self.amount_due,"month_name":self.my_month})


        # record = self.env['wizard.total.calculate.o2m'].search([('sidd_challenge_2','=',self.act)])
        # record.create({"sidd_challenge_2":self.act,"paid_fees":self.paid_fees,"amount_due":self.amount_due})
        # record.write({"sidd_challenge_2":self.act,"paid_fees":self.paid_fees,"amount_due":self.amount_due})
        # print "RECORD============================",record
        # print "TYPE============================",type(record)
        # print "RECORD============================",record[0]
        # rec_found = self.env['wizard.total.calculate.o2m'].search([('sidd_challenge_2','=',self.act)])
        # for each in rec_found:
        #     print "RECORD EACH=============================================",each.id




class wizard_total_calculation_o2m(models.Model):
    _name = 'wizard.total.calculate.o2m'

    sidd_challenge_2 = fields.Many2one('student.student','Name')
    paid_fees = fields.Integer('Paid Fees:')
    amount_due = fields.Integer('Amount Due:')
    month_name = fields.Char('Month Name:')








