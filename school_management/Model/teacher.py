import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8
import datetime

class teacher(models.Model):
    _name = 'teacher'

    name = fields.Char('Name', required=1)
    user_id = fields.Many2one('res.users','Select User:')
    address = fields.Text('Address')
    pincode = fields.Char('Pincode')
    telephone = fields.Char('Telephone')
    birthdate = fields.Date('Birthdate')
    joindate = fields.Datetime('Join Date')
    ID_NO = fields.Integer('ID_NO')
    #fees_amt = fields.Float('Fees')
    active = fields.Boolean('Active',  default=1)
    Experience = fields.Selection([('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four')], 'Stand.')

    student_id = fields.Many2one('student','Student ID :')
    # subject = fields.Many2many('subject','subject_teacher_rel','sub_id','teacher_id')
    # Choose_subject = fields.One2many('subject','choose_teacher','Choose Teacher :')
    teacher_stud = fields.One2many('student','choose_teacher','Teacher Student Relation:')





