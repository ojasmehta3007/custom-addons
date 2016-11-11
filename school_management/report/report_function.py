

import pytz
from openerp.osv import osv
from openerp.report import report_sxw
from datetime import datetime

class TrainingReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(TrainingReport, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'get_current_time':self.get_current_time,
            'an_custom':self.an_custom,
            # 'get_birthdate_teacher':self.get_birthdate_teacher,

                    # 'get_data':self.get_data,
            })

    def get_current_time(self):
        a = datetime.today()
        time_zone='Asia/Calcutta'
        tz = pytz.timezone(time_zone)
        tzoffset = tz.utcoffset(a)
        a = a + tzoffset
        return a
    #
    # def mycusotm(self):
    #     return "hello ESC"

    def an_custom(self):
        str="<p>HELLO RAW</p>"
        return str
    # def get_current_time(self):
    #     current_time=datetime.now()
    #     # ti = datetime.utcfromtimestamp(self)
    #     # print "ti===========================",ti
    #     # t = ti.timetuple()
    #     print"current_timecurrent_time==============================",current_time
    #     # print "Updated Time========================================",t
    #     return current_time




    # def get_data(self):
    #     return "<p>Sale Order</p>"

    # def get_birthdate_teacher(self):
    #     context = dict(self._context or {})
    #     active_ids = context.get('active_ids', False)
    #     for each in active_ids:
    #         each = self.env['teacher'].browse(active_ids)
    #         print "*******************######################",each.name
    #         print "**********************************##########",each.birthdate
    #         return each.birthdate


class ReportTrainingQwb(osv.AbstractModel):
    #    name must be report.module_name.template_id
    _name='report.school_management.template_student'
    _inherit ='report.abstract_report'
    _template = 'school_management.template_student'
    _wrapped_report_class = TrainingReport

class ReportTrainingQwb(osv.AbstractModel):
    #    name must be report.module_name.template_id
    _name='report.school_management.template1'
    _inherit ='report.abstract_report'
    _template = 'school_management.template1'
    _wrapped_report_class = TrainingReport


