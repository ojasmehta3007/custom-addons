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


class salary(models.TransientModel):
    _name = 'salary'
    # _inherit = 'teacher'


    name = fields.Char('Name:')

    teacher_sal = fields.Integer('Teacher Salary')



    @api.model
    def default_get(self, fields_list):
        res = super(salary, self).default_get(fields_list)
        context = dict(self._context or {})
        print 'hello'
        active_ids = context.get('active_ids', False)
        active_ids_new = context.get('active_ids',False)

        print 'world'
        a = ""

        for each in active_ids:
            each = self.env['teacher'].browse(active_ids)
            print each
            print 'Done'
            print each.name
            print each.address
            print each.pincode
            print each.telephone
            print each.birthdate
            print each.joindate
            print each.ID_NO
            print each.active
            res.update({'name':str(each.name),'teacher_sal':each.ID_NO})
            print "res====",res
            print "context====",self._context
            return res



        # if active_id and active_id_new:
        #     inv = self.env['teacher'].browse(active_id)
        #     inv2 = self.env['student'].browse(active_id_new)
        #
        #     # print inv2.teacher_sal
        #     print inv.name
        #     print inv2.fees_amt
        #     # print inv.teacher_sal
        #     # return inv.name
        #     print 'above'
        #     print 'hi'
        #     res.update({'name':str(inv.name),'teacher_sal':inv2.fees_amt})
        #     print "res+++++",res
        #     print "context++++++",self._context
        #     return res


    # def teach_sal(self):
    #     teach_salary = self.teacher_sal
    #
    #




