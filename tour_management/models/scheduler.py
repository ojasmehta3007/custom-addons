from openerp import models, fields, api, _
from openerp.exceptions import ValidationError
from datetime import datetime
import pytz

class scheduler_spreadsheet(models.Model):

    _inherit='res.partner'

    @api.model
    def get_data_from_google_spreadsheet_scheduler(self):

        print " Hello Scheduler is Running Perfect"