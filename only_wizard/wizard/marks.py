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

    name = fields.Char('Name')
    marks_child_O2M = fields.One2many('marks.child','marks_parent_M2O','Calling Child:')


    @api.model
    def default_get(self, fields_list):
        res = super(marks, self).default_get(fields_list)
        context = dict(self._context or {})
        print "default get",context
        active_id = context.get('active_id', False)
        print 'active ID:',active_id
        print 'hello',self.env['student'].browse(active_id).name
        # wiz = self.env['marks.child'].create({'name': self.})
        res.update({'name':self.env['student'].browse(active_id).name})
        print "wiz+================"
        if active_id:
            each = self.env['student'].browse(active_id)
            print each
            print 'Hi'
            # second table column
            print each.student_marks_rel
            print str(each.student_marks_rel.subject_name_ref.name)
            print "=============DEFUALT GET END================"
            # for line in each.student_marks_rel:
            #     vals = {}
            #     print "=======line======",line
            #     vals.update({'marks_of_student': line.marks_of_student,
            #              'subject_name_ref': line.subject_name_ref.id,
            #              'marks_parent_M2O': wiz.id})
            #     self.env['marks.child'].create(vals)
        return res

    @api.multi
    def myfunction(self):
        print "=========================MY FNCTN================================"
        inv = self.name
        print "inv++++++++++++++++",inv

        marks_child_O2M = self.env['student'].browse(self._context.get('active_id')).student_marks_rel

        print "M2O================",marks_child_O2M
        for line in marks_child_O2M:
            vals = {}
            print "=======line======",line
            self.env['marks.child'].create({'marks_of_student': line.marks_of_student,
                        'subject_name_ref': line.subject_name_ref.id,
                        'marks_parent_M2O': self.id})

        return{
            'name': _('Wizard'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'marks',
            'res_id': self.id,
            'type': 'ir.actions.act_window',
            'target' : 'new',
        }


















            # return {
            # 'name': _('Returned Picking'),
            # 'view_type': 'form',
            # 'view_mode': 'form',
            # 'res_model': 'marks',
            # 'res_id': wiz.id,
            # 'type': 'ir.actions.act_window',
            # 'target' : 'new',
            #         }


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









            # print str(each.subject1)
            # print str(each.subject2)
            # print str(each.subject3)
            # print str(each.percentage)
            # print 'below'
            # res.update({'subject10':each.subject1,'subject20':each.subject2,'subject30':each.subject3,'percentage_new':each.percentage})
            # print "res====",res
            # print "context====",self._context
            # return res



