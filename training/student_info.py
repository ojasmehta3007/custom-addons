from openerp import models
from openerp import api, _
from openerp.tools import float_compare, float_is_zero
from openerp import workflow, fields


class student_info(models.Model):
    _name = 'student.info'
    _rec_name='student_names'

    # student_name = fields.Char('Name')

    subject_rel=fields.One2many('subject.info','select_student_name','sel subject')

    student_names = fields.Char('Name')

    address = fields.Char('address')

    @api.multi
    def start_wizard(self):
            print 'xxxx'

            context = self._context or {}
            print 'xxxx'

            values = {"name_wizard":self.student_names}
            print 'xxxx'
            wizard_id = self.env['record'].create(values)
            print 'xxxx',wizard_id.id
            return {
                        'name': 'NEw Wizard',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'record',
                        'res_id': wizard_id.id,
                        'type': 'ir.actions.act_window',
                        'target': 'new',
                        'context': context
            }





