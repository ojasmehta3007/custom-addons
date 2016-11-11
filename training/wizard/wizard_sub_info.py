from openerp import models, fields, api

# from openerp.tools.translate import _

class wizard_sub_info(models.TransientModel):
    _name = "wizard.sub.info"
    _description = "Make record"

    record_id = fields.Many2one('record','Selct student')
    phy=fields.Integer("PHy")
    chem=fields.Integer("chem")
    percent=fields.Float("%")