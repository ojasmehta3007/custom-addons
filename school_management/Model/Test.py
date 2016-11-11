import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8

class teacher(models.Model):
    _name = 'teacher'
    _inherit = 'teacher'

    regno = fields.One2many('subject','choose_teacher','Rgno:')
    exam_id = fields.Integer('Exam ID:')
