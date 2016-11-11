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

class marks(models.TransientModel):
    _name = 'marks'

    # student_name = fields.Char('Student Name:')
    subject10 = fields.Integer('Physics:')
    subject20 = fields.Integer('Chemistry')
    subject30 = fields.Integer('Maths')
    percentage_new = fields.Float('Percentage : ')
     # total_marks = fields.Integer('Total Marks')
    marks_child_O2M = fields.One2many('marks.child','marks_parent_M2O','Calling Child:')

    @api.model
    def default_get(self, fields_list):
        res = super(marks, self).default_get(fields_list)
        context = dict(self._context or {})
        active_ids = context.get('active_ids', False).subject_rel
        print 'active ID:',active_ids
        print 'hello'
        for each in active_ids:
            each = self.env['student'].browse(active_ids)
            print each
            print 'Hi'
            print str(each.subject1)
            print str(each.subject2)
            print str(each.subject3)
            print str(each.percentage)
            # res.update({'subject10':each.subject_rel.subject1})


            #
            # for line in self.marks_child_O2M:
            #     vals = {}
            #     print "=======line======",line
            #     vals.update({'subject10': line.subject10,
            #              'subject20': line.subject20,
            #              'subject30': line.subject30,
            #              'percentage_new': line.percentage_new,
            #              'marks_parent_M2O': line.marks_parent_M2O.id})
            #     self.env['marks.child'].create(vals)
            #     print "vals==========",vals
            #
            # return {
            # 'name': _('Returned Picking'),
            # 'view_type': 'form',
            # 'view_mode': 'form',
            # 'res_model': 'marks',
            # 'res_id': marks,
            # 'type': 'ir.actions.act_window',
            # 'target' : 'new',
            #         }

            print "res============",res
            print "context============",self._context
            return res




            # print str(each.subject1)
            # print str(each.subject2)
            # print str(each.subject3)
            # print str(each.percentage)
            # print 'below'
            # res.update({'subject10':each.subject1,'subject20':each.subject2,'subject30':each.subject3,'percentage_new':each.percentage})
            # print "res====",res
            # print "context====",self._context
            # return res



