import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8

class test1(models.Model):
    _inherit = 'res.partner'

    priority_partner = fields.Boolean('Priority Partner: ')
    registration_date = fields.Date('Registration Date:')
    liability_card = fields.Char('Liability Card Number :')






