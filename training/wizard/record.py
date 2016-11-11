from openerp import models, fields, api

# from openerp.tools.translate import _

class record(models.TransientModel):
    _name = "record"
    _description = "Make record"

    name_wizard = fields.Char('name')

    name_stdent=fields.One2many('wizard.sub.info','record_id','name')
    total_pertage=fields.Float("%")
# active_id=self._context.get('active_id')

    @api.model
    def default_get(self, fields):
        res = super(record, self).default_get(fields)


        print "+++++++++++++++++++++++++++++++++++++++++==def_get"


        return res








    @api.multi
    def start_wizards_result(self):
            self.env['wizard.sub.info'].search([('id', '!=', None)]).unlink()
            print 'xxxx'

            active_id=self._context.get('active_id')
            print 'xxxx'
            print active_id

            counter=0
            total_pertage1=0

            student_records=self.env["student.info"].browse(active_id)

            for each in student_records.subject_rel:
                counter=counter+1

                print "each",each
                ans=(each.phy+each.chem)*0.5
                total_pertage1=ans+total_pertage1

                self.env['wizard.sub.info'].create({"record_id":self.id,"phy":each.phy,"chem":each.chem,"percent":ans})

            total=total_pertage1/counter
            self.update({"total_pertage":total})
            self.update({"name_wizard":self.name_wizard+"xzc"})


            print 'xxxx'
            return {
                        'name': 'NEw Wizard',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'record',
                        'res_id': self.id,
                        'type': 'ir.actions.act_window',
                        'target': 'new',
                        'context': self._context
            }
