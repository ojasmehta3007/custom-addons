from openerp import models, fields, api

# from openerp.tools.translate import _

class grade(models.TransientModel):
    _name = "grade"
    _description = "Make grade"


    name_stdent_infos=fields.Char("name")

    grade_infos = fields.Char('grade')



    @api.model
    def default_get(self, fields):
        res = super(grade, self).default_get(fields)
        active_id=self._context.get('active_id')
        print "+++++++++++++++++++++++++++++++++++++++++==",active_id

        inv1=self.env['subject.info'].browse(active_id)
        #

        if inv1.percent<40.00:
            grade_info="C"

        if inv1.percent>60.00:
            grade_info="A"

        else:
            grade_info="C"


        student=inv1.select_student_name.student_names

        res.update({'name_stdent_infos':student,'grade_infos':grade_info})
        print "res+++++",res
        print "context++++++",self._context
        return res






