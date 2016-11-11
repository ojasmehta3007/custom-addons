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
{
    'name' : 'Management.School Management',
    'version' : '1.1',
    'author' : 'OpenERP SA',
    'category' : 'General',
    'description' : """

    """,
    'depends' : ['base','sale'],
    'data': [
        'data/student_view_data.xml',
        'security/security_view.xml',
        'security/ir.model.access.csv',
        'view/student_view_form.xml',
        'view/teacher_view_form.xml',
        'view/employee_information_view_form.xml',
        'view/attendance_information_view_form.xml',
        'view/info_search_view_form.xml',
        'view/subject_view_form.xml',
        'view/achievements_view_form.xml',
        'view/test_view_form.xml',
        'view/alumni_view_form.xml',
        'view/customer_liability_view_form.xml',
        'view/test1_view_form.xml',
        'view/test2_view_form.xml',
        'view/priority_view_form.xml',
        'view/partner_view_form.xml',
        'wizard/salary_view_form.xml',
        'wizard/marks_view_form.xml',
        'wizard/marks_child_view.xml',
        'wizard/menu_wizard_view_form.xml',
        'report/reports.xml',
        'report/template1.xml',
        'report/template2.xml',


    ],


     'css': ['static/src/css/mycss.css'],

    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
