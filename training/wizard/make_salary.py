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

from openerp import models, fields, api

# from openerp.tools.translate import _

class teacher_salary(models.TransientModel):
    _name = "teacher.salary"
    _description = "Make Salary"

    name = fields.Char('Name')
    salary = fields.Float('Salary')
    extra = fields.Float('Extra Salary')

    @api.model
    def default_get(self, fields):
        res = super(teacher_salary, self).default_get(fields)
        # context = dict(self._context)
        active_ids=self._context.get('active_ids')
        total_salary=0
        allname =""
        if active_ids:



            for each in active_ids:
                inv=self.env['college.teacher'].browse(each)
                print inv.name
                allname=allname +str(inv.name)+ " ,  "

                total_salary+=inv.salary
                print  total_salary





            res.update({'name':allname,'salary':total_salary,'extra':200})
            print "res+++++",res
            print "context++++++",self._context
            return res
# str(inv.name)













#
# @api.model
# def default_get(self, fields_list):
# res = super(salary, self).default_get(fields_list)
#    context = dict(self._context or {})
# print 'hello'
# active_id = context.get('active_id', False)
# print 'world'
# a = ""
# if active_id:
# inv = self.env['teacher'].browse(active_id)
# print inv.name
# # print inv.teacher_sal
# # return inv.name
# print 'above'
# print 'hi'
# res.update({'name':str(inv.name),'teacher_sal':12000})
# print "res+++++",res
# print "context++++++",self._context
# return res
#
















    #     data = self.trans_rec_get()
    #     if 'name' in fields:
    #         res.update({'name': data['name']})
    #     if 'salary' in fields:
    #         res.update({'salary': data['salary']})
    #     if 'extra' in fields:
    #         res.update({'extra': data['extra']})
    #     return res
    #
    # @api.multi
    # def trans_rec_get(self):
    #     context = self._context or {}
    #     name = salary = 0
    #     lines = self.env['college.teacher'].browse(context.get('active_ids', []))
    #     for line in lines:
    #         name += line.name
    #         salary += line.salary
    #     extra = salary
    #
    #     return {'name': name, 'salary': salary, 'extra': extra}
