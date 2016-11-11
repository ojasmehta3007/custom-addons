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



    name = fields.Char('Name')
    user_id = fields.Many2one('res.users','Select User:')
    image = fields.Binary('Image')
    address = fields.Text('Address')
    pincode = fields.Char('Pincode')
    telephone = fields.Char('Telephone')
    birthdate = fields.Date('Birthdate')
    age = fields.Integer('Age')
    joindate = fields.Datetime('Join Date')
    roll_no = fields.Integer('Roll Number')
    fees_amt = fields.Float('Fees')
    active = fields.Boolean('Active',  default=1)
    stand = fields.Selection([('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four')], 'Stand.')
    stage = fields.Selection([('documentupload', 'Document Uploaded Successfully'), ('Verification', 'Verification'), ('finalreview', 'Final Review'), ('disbursed', 'Document Ready To Disbursed')])

    details = fields.Text('Details')
    choose_teacher1 = fields.Many2one('teacher','Choose Teacher :')

    choose_teacher = fields.One2many('teacher','student_id','Student Teacher Rel:')
    achievements = fields.One2many('achievements','choose_student','Achievements are :')
    subject_rel = fields.One2many('subject','select_student','Student Subject List:')


    # stud_alumni_id = fields.Many2one('alumni','Alumni ID:')


    @api.multi
    def myfucntion(self):
        Student_Name = self.name
        Student_address = self.address
        Student_pincode = self.pincode
        Student_telephone = self.telephone
        concatenate = "Name : %s \n Address: %s \n Pincode: %s \n Telephone: %s" %(Student_Name,Student_address,Student_pincode,Student_telephone)
        self.details = concatenate

    @api.multi
    def write(self,vals):
        print "vals==================",vals
        context = dict(self._context or {})
        print "context==================",self._context
        list = ['0','1','2','3','4','5','6','7','8','9']
        if vals.get('name',False):
            print True
            for obj in vals.get('name'):
                if obj in list:
                    raise except_orm(_("Warning"))
                # else:
                #     return super(student,self).write(vals)
        return super(student, self).write(vals)



    @api.model
    def create(self, my):
        print "vals",my
        list = ['0','1','2','3','4','5','6','7','8','9']
        if my.get('name',False):
            print "TRUE++++++++++++++++++++++++++",True
            print "vals=================================",my
            for obj in my.get('name'):
                if obj in list:
                    raise except_orm(_("Warning"))
                # else:
                #     return super(student,self).create(vals)
        return super(student, self).create(my)



    @api.multi
    def copy(self,default=None):
        default.update(
             fees_amt=_("%d") % (12000),
             stand = ("%s" % ('two'))
        )
        return super(student, self).copy(default)



    @api.multi
    def unlink(self):
        if  self.active == 1:
            raise except_orm(_("Warning"))
        else:
            pass
        return super(student, self).unlink()

    @api.multi
    @api.onchange('birthdate')
    @api.depends('pincode')
    def mycustom(self):
        print "Inside depends"
        a = self.birthdate
        print "vals====================",a
        curr_birth_date = datetime.strptime(str(self.birthdate),"%Y-%m-%d")
        print "ONTHEFLY==========================",curr_birth_date.year
        curr_year = datetime.now().year
        print "curr_time====",curr_year
        self.age = curr_year - curr_birth_date.year

        # strings = datetime.strftime(curr_birth_date,"%Y-%m-%d")
        # print "strings===============",strings




    # @api.multi
    # def download(self):
    #     print "Download-=========================="
    #     url = ""
    #     print ("File Reading Done...!!!!")
    #     return{
    #         'res_model': 'student',
    #         'type': 'ir.actions.act_url',
    #         'target' : 'current',
    #         'url' : url,
    #     }



    # @api.model
    # def default_get(self, fields):
    #     ticks =  strftime("%Y-%m-%d %H:%M:%S", gmtime())
    #     res = super(student, self).default_get(fields)
    #     res.update({'pincode':401107,'joindate':ticks})
    #     return res


#
# -------------------------------------------

    # @api.multi
    # def birthdate(self):
    #     new_birth = self.birthdate
    #     print "NEW :",new_birth








 # @api.one
 #    def copy(self, default=None):
 #        default = dict(default or {})
 #        default.update(
 #            code=_("%s (copy)") % (self.code or ''),
 #            name=_("%s (copy)") % (self.name or ''))
 #        return super(AccountJournal, self).copy(default)













