from openerp import models
from openerp import api, _
from openerp.tools import float_compare, float_is_zero
from openerp import workflow, fields


class suject_info(models.Model):
    _name = 'subject.info'


    select_student_name = fields.Many2one('student.info','Selct student')
    phy=fields.Integer("PHy")
    chem=fields.Integer("chem")
    percent=fields.Float("%")


    @api.multi
    @api.onchange('percent')
    def sal_count_onchg(self):
        self.percent=(self.chem+self.phy)/2