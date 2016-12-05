# from openerp import models, fields, api, _
# from openerp.exceptions import ValidationError
# from datetime import datetime
#
#
# class Res_Company(models.Model):
#
#     _inherit='res.company'
#
#     stock_mngt= fields.Boolean('Stock Management')
#     stock1 = fields.Many2one('account.account', string="Account 1")
#     stock2 = fields.Many2one('account.account', string="Account 2")
#     stock3 = fields.Many2one('account.account', string="Account 3")
#     stock4 =  fields.Many2one('account.journal', string="Account Journal")
#
#     @api.onchange('stock_mngt')
#     def onchange_stocks(self):
#
#         if self.stock_mngt == False:
#             self.stock1 = ""
#             self.stock2 = ""
#             self.stock3 = ""
#             self.stock4 = ""
#
#
