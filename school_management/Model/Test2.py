import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8

class teacher(models.Model):
    _name = 'teacher2'
    _inherit = 'teacher'


    hall_ticket2 = fields.Many2one('student','Exam ID/Hall-Ticket Name:')
    exam_center = fields.Char('Exam Center:')
