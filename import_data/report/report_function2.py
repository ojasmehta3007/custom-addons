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

class call_report(report_sxw.rml_parse):
    _inherit = 'res.users'

    def __init__(self, cr, uid, name, context):
        super(call_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'get_current_time':self.get_current_time,
            'get_sale_order_line':self.get_sale_order_line,
            })

    def get_current_time(self):
        a = datetime.today()
        time_zone='Asia/Calcutta'
        tz = pytz.timezone(time_zone)
        tzoffset = tz.utcoffset(a)
        a = a + tzoffset
        return a


    def get_sale_order_line(self,vals):
        # print "SELF=====================",self
        # print "Vals=====================",vals
        # print "VALS=====================",vals.partner_id
        # print "VALS=====================",vals.partner_id.name
        # print "VALS=====================",vals.partner_id.id 6
        # print "VALS=====================",self.localcontext
        c_user_id = vals.id
        print "CUSTOM USER ID============================",c_user_id
        single_row = []
        total_comm_amount = 0
        grand_total_amount = 0
        record = self.pool.get('sale.order').search(self.cr, self.uid, [('user_id','=',c_user_id)])
        print "RECORD=====================",record
        for each in record:
            # print "EACH============================",each
            new_record = self.pool.get('sale.order').browse(self.cr, self.uid, each)
            if new_record.invoice_status == 'invoiced':
                # print "INVOICED STATUS=============\n\n",new_record.id
                for my in new_record:
                    comm_amount = (my.amount_total * vals.commission_field) / 100
                    # print "Partner_id",vals.partner_id.name
                    # print "NAME====================",my.name
                    # print "Amount Total============",my.amount_total
                    # print "Commission Field===========",vals.commission_field

                    total_comm_amount = total_comm_amount + comm_amount
                    grand_total_amount = grand_total_amount + my.amount_total

                    single_row.append({'username':vals.partner_id.name,'donesalesorder':my.name,'amounttotal':my.amount_total,'commissionamount':comm_amount})
                    print "SINGLE ROW DICT:=========================",single_row

                    # single_row = single_row + "<tr><td>" +str(vals.partner_id.name)+ "</td><td>" +str(my.name)+ "</td><td>" +str(my.amount_total)+ "</td><td>" + str(comm_amount)+ "</td></tr>"
                    # print "SINGLE TOW============",single_row
                    # total_comm_amount = total_comm_amount + comm_amount
                    # grand_total_amount = grand_total_amount + my.amount_total
                    # print "TOTAL COMM AMOUNT================",total_comm_amount
                    # print "GRAND TOTAL AMOUNT================",grand_total_amount
        return single_row
        # return single_row + "<tr><td>" + "</td><td>" + "</td><td><b>Grand Total Amount</b>" +str(grand_total_amount)+ "</td><td><b>Total Commission Amount</b> :  " +str(total_comm_amount)+ "</td></tr>"

class ReportTrainingQwb(osv.AbstractModel):
    #    name must be report.module_name.template_id
    _name='report.import_data.commission_template'
    _inherit ='report.abstract_report'
    _template = 'import_data.commission_template'
    _wrapped_report_class = call_report
