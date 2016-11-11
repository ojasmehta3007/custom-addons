# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8
from openerp.exceptions import except_orm,UserError, ValidationError
from datetime import datetime

class achievements(models.Model):
    _name = 'achievements'
    _rec_name = 'achieve'

    achieve = fields.Text('Achievements : ')
    choose_student = fields.Many2one('student','Choose Student :')
    s_date = fields.Datetime('Start Date:')
    e_date = fields.Datetime('End Date:')
    time = fields.Char('Time Difference:')
    state = fields.Selection([('start','Start'),('resume','Resume'),('stop','Stop')])

    #achieve = fields.Many2many('subject','subject_teacher_rel','subject_id','teacher_id')



    @api.multi
    def start_state(self):
        st = datetime.now()

        self.write({
        'state': 'start',
        's_date' : st,
        })

    @api.multi
    def resume_state(self):
        self.write({
            'state':'resume',
        })

    @api.one
    def stop_state(self):


        st = datetime.strptime(str(self.s_date),"%Y-%m-%d %H:%M:%S")
        print "dt=================",st
        # dt1 = str(dt)
        # print "dt1=================",dt1
        et = datetime.now()
        print "et_et ==========================",et
        # et = datetime.strptime(str(et_et),"%Y-%m-%d %H:%M:%S")

        diff = et - st
        print "diff===================",diff

        self.write({
            'state' : 'stop',
            'e_date' : et,
            'time' : diff ,
        })

        # self.t_diff = diff
        # return self.t_diff

        # self.e_date = datetime.now()
        # return  self.e_date



