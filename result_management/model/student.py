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

import re
import time
import datetime
from datetime import datetime
from time import gmtime, strftime


class student(models.Model):
    _name = 'student'

    name = fields.Char('Student Name:')
    user_id = fields.Many2one('res.users','Select User:')
    student_marks_rel = fields.One2many('marks','student_name_ref','Student Marks:')
    student_teacher = fields.Many2one('teacher','Select Your Teacher:')
    # stud_sub_rel = fields.One2many('')

    @api.multi
    def show_result(self,context=None):
        print "################################",context
        wiz = self.env['wizard.details'].create({'name': self.name})
        print "Self NAME=========",self.name
        print "wizard+++++++++++", wiz.name
        for line in self.student_marks_rel:
            vals = {}
            print "=======line======",line
            vals.update({'marks_of_student': line.marks_of_student,
                         'subject_name_ref': line.subject_name_ref.id,
                         'wiz_id': wiz.id})
            self.env['wiz.marks'].create(vals)

        # wiz_id = self.env['wizard.details'].create(vals)
        return {
            'name': _('Returned Picking'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wizard.details',
            'res_id': wiz.id,
            'type': 'ir.actions.act_window',
            'target' : 'new',
                    }

    # def _search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False, access_rights_uid=None):
    #     # if context.get('user_id'):
    #     #     print "Inside Context++++++++++++++++++++++++++++"
    #     print "contetx==+++++++++++++++++",context.get('name')
    #
    #     print "contetx==+++++++++++++++++",context
    #     return super(student, self)._search( cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count, access_rights_uid=access_rights_uid)



    # def _search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False, access_rights_uid=None):
    #     """ Override _search to order the results, according to some employee.
    #     The order is the following
    #
    #      - limit (limited leaves first, such as Legal Leaves)
    #      - virtual remaining leaves (higher the better, so using reverse on sorted)
    #
    #     This override is necessary because those fields are not stored and depends
    #     on an employee_id given in context. This sort will be done when there
    #     is an employee_id in context and that no other order has been given
    #     to the method. """
    #     if context is None:
    #         context = {}
    #     print "contetx==+++++++++++++++++",context.get('name')
    #
    #     print "contetx==+++++++++++++++++",context
    #     return super(student, self)._search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count, access_rights_uid=access_rights_uid)

