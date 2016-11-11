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

class info_search(models.Model):
    _name = 'info.search'

    student_name = fields.Char('Students Name : ')
    student_rollno = fields.Integer('Students Roll No : ')


    student_details = fields.Text('Student Details : ')

    # @api.multi
    # def search_function(self):
    #     s_name = self.student_name
    #     s_rollno = self.student_rollno
    #     result = "Student Name : %s \n Roll No: %d " %(s_name,s_rollno)
    # + str(each.pincode) + str(each.telephone) + each.birthdate + each.joindate + str(each.fees_amt) + each.active + each.stand


# +str(each.roll_no)+"\nStudent Address : "+each.address+"\nStudent Pincode : "+str(each.pincode)+"\nStudent Telephone"+str(each.telephone)+"\nStudent Birthdate :"+each.birthdate+"\nStudent Joined Date: "+each.joindate+"\nStudent Fees Amount"+str(each.fees_amt)+"\nStudent Standard : "+each.stand


    #     self.student_details = result


    @api.multi
    def search_records(self):
        r_name = self.student_name
        r_rollno = self.student_rollno

        # r_address = self.student_address

        data = self.env['student'].search(['|',('name','=',r_name),('roll_no','=',r_rollno)])
        #print "======data====",data
        loc_var =""
        for each in data:
                loc_var += "Student Name: "+each.name+"\nStudent Roll No: "+str(each.roll_no)+"\nStudent Address : "+each.address+"\nStudent Pincode : "+str(each.pincode)+"\nStudent Telephone"+str(each.telephone)+"\nStudent Birthdate :"+each.birthdate+"\nStudent Joined Date: "+each.joindate+"\nStudent Fees Amount : "+str(each.fees_amt)+"\nStudent Standard : "+each.stand+"\n"+"\n =====Next Record :=====\n"

        self.student_details = loc_var


    @api.multi
    def browse_records(self):
        r_name = self.student_name
        r_rollno = self.student_rollno

        # r_address = self.student_address

        data = self.env['student'].search(['|',('name','=',r_name),('roll_no','=',r_rollno)])
        #print "======data====",data
        loc_var =""
        for each in data:
            each = self.env['student'].browse(each.id)
            loc_var += "Student Name: "+each.name+"\nStudent Roll No: "+str(each.roll_no)+"\nStudent Address : "+each.address+"\nStudent Pincode : "+str(each.pincode)+"\nStudent Telephone"+str(each.telephone)+"\nStudent Birthdate :"+each.birthdate+"\nStudent Joined Date: "+each.joindate+"\nStudent Fees Amount : "+str(each.fees_amt)+"\nStudent Standard : "+each.stand+"\n"+"\n =====Next Record :=====\n"

        self.student_details = loc_var






       # self.r_rollno = ""

            # id = data.browse([each.name])
            # print "=====id====",id.id
            # return id




