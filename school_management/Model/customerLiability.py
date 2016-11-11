import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8


class customer_liability(models.Model):
    _name = 'customer.liability'

    customer = fields.Many2one('res.partner','Customer:')
    points_earned = fields.Float('Points Earned:')
    state = fields.Selection([('draft','Draft'),('approved','Approved'),('cancelled','Cancelled')],default = "draft")


    @api.one
    def draft_progressbar(self):
        self.write({
        'state': 'draft',
        })

    @api.one
    def approved_progressbar(self):
        self.write({
        'state': 'approved',
        })

    @api.one
    def cancel_progressbar(self):
        self.write({
        'state': 'cancelled',
        })

