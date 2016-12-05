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
    'name' : 'Import Data',
    'version' : '1.1',
    'author' : 'OpenERP SA',
    'category' : 'General',
    'description' : """
    """,
    'depends' : ['base','report','mail','sale'],
    'data': [
        'view/task1_view.xml',
        'view/binary_view_data.xml',
        'view/task_view.xml',
        'view/task2_view_file.xml',
        'view/task3_view.xml',
        'view/task4_view.xml',
        'view/task5_view.xml',
        # 'view/task6_view.xml',
        'view/task7_view.xml',
        'report/reports.xml',
        'report/commission_template.xml',
        'report/student_report_download.xml',
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
