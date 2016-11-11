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

import re
import time
import datetime
from datetime import datetime
from time import gmtime, strftime

class priority_table(models.Model):
    _name = 'priority.table'

    name = fields.Text('Priority Name:')
    set_priority = fields.Selection([('true','True'),('false','False')],string ='Set Priority:')
    select_name = fields.Many2one('res.partner','Please Select Your Name:')



    @api.model
    def create(self,vals):
        print "Inside Create===================",self._context


        new_id = vals['select_name']
        print "NEW ID==================================",new_id
        # new_id = self._context.get('params')['id']
        # print "NEW ID================================",new_id

        b = self.env['priority.table'].search(['&',('select_name','=',new_id),('set_priority','=','true')])

        for each in b:
            print "====================B IS PRINTING=================",each.id
            print "=====================values======================",each.set_priority
            if vals['set_priority'] == 'true':
                print "Inside=================Create ONLY==============================="
                each.set_priority = 'false'
        return super(priority_table, self).create(vals)

    @api.multi
    def write(self,vals):
        print "Inside WRITE===================",self._context


        # new_id = self._context.get('params')['id']
        # print "NEW ID=WRITE===============================",new_id
        print "PARTNER ID===============================",self.select_name
        new_id = self.select_name.id
        b = self.env['priority.table'].search(['&',('select_name','=',new_id),('set_priority','=','true')])

        for each in b:
            print "====================B IS PRINTING(WRITE)=================",each.id
            print "=====================values(WRITE)======================",each.set_priority
            if vals['set_priority'] == 'true':
                print "Inside=================WRITE ONLY==============================="
                each.set_priority = 'false'
        return super(priority_table, self).write(vals)





    #
    # @api.multi
    # def write(self,vals):
    #     print "Inside write+++++++++++++++++++++++++++++++++++++++++++++++++++",self._context
    #
    #     new_id = self._context.get('params')['id']
    #     print "NEW ID+++++++++++++++++++++++++++++++++++++++++++++++++",new_id
    #
    #     for each in self.select_name:
    #         b = self.env['priority.table'].search(['&',('select_name','=',new_id),('set_priority','=','true')])
    #         print "+++++++++++++++++++++++values+++++++++++++++++++++++++++++++",b.set_priority
    #
    #
    #     if vals['set_priority'] == 'true':
    #         print "Inside Write ONLY++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    #         b.set_priority = 'false'
    #     return super(priority_table, self).write(vals)


class relation_priority(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'


    relation =  fields.Many2one('priority.table','Relation :')




    @api.onchange('partner_id')
    def change(self):
        a = self.partner_id
        print "a================================",a.id

        id=0

        #Abhishek Help
        # for each in a.check_priority:
        #     print "each=============================",each.id
        #     if each.set_priority == 'true':
        #         print "True================"
        #         id = each.id
        #
        # print "ID============",id
        # self.relation = id

        inv = self.env['priority.table'].search(['&',('select_name','=',a.id),('set_priority','=','true')])
        for each in inv:
            print "INV===================================",each
            print "VALUES=================================",each.set_priority
            id = each.id

            # if each.set_priority == 'true':


        print "ID==============",id
        self.relation = id



    # self.relation=id




