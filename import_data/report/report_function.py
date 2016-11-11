from openerp.osv import fields, osv, expression  # V7
from openerp import models, fields, api, _  # v8
import base64
import xlrd
from datetime import datetime
import calendar
import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8
from openerp.exceptions import except_orm,UserError, ValidationError



import pytz
from openerp.osv import osv
from openerp.report import report_sxw
from datetime import datetime

class TrainingReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(TrainingReport, self).__init__(cr, uid, name, context=context)
        print "INSIDE TRANING REPORT SELF===============",self
        self.localcontext.update({
            'get_current_time':self.get_current_time,
            'get_sale_order_line':self.get_sale_order_line,
            })


    def get_current_time(self):
        print "INSIDE======================"
        a = datetime.today()
        time_zone='Asia/Calcutta'
        tz = pytz.timezone(time_zone)
        tzoffset = tz.utcoffset(a)
        a = a + tzoffset
        print "A==========================",a
        return a


    def get_sale_order_line(self,cr,uid,context):
        print "INSIDE LINE=====================",self
        print "INSIDE LINE=====================",context
        # obj = self.env['sale.order'].


class ReportTrainingQwb(osv.AbstractModel):
    #    name must be report.module_name.template_id
    _name='report.import_data.commission_template'
    _inherit ='report.abstract_report'
    _template = 'import_data.commission_template'
    _wrapped_report_class = TrainingReport



