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
    student_marks_rel = fields.One2many('marks1','student_name_ref','Student Marks:')

    @api.multi
    def show_result(self):
        context = dict(self._context or {})
        active_id = context.get('active_id', False)
        wiz = self.env['marks'].create({'name': self.name})
        print "wiz===========",wiz
        print "wiz name==============",wiz.name
        print self.name
        print wiz
        context = dict(self._context or {})
        # a = context.get('params', False)
        # print "a===============",a['id']

        i = self._context
        print "i==========",i



        b = self.env['marks']._context.copy()
        print "before b",b
        b.update({'wiz_id':wiz.id})
        print 'button click after',b

        return {
            'name': _('Returned Picking'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'marks',
            'res_id': wiz.id,
            'type': 'ir.actions.act_window',
            'target' : 'new',
                    }


        # print active_id

