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


class adding(models.Model):
    _name = 'adding'


    name = fields.Char('Just Name:')
    address = fields.Char('Address:')

    @api.multi
    def my(self):
        my_id = self._context.get('params')['id']
        print "CONTEXT++++++++++++",self._context




        result = {
            'name' : 'RETURNING',
            'view_type' : 'form',
            'res_model' : 'mix',
            'context' : {'default_name': my_id},
            'type' : 'ir.actions.act_window',
            'view_mode' : 'form'

                 }
        return result



class mix(models.Model):
    _name = 'mix'

    name = fields.Many2one('adding',string='NAME:')
    address = fields.Char('Addrtess')


    @api.multi
    @api.onchange('name')
    def my2(self):
        self.address = self.name.address
        print "MIX CONTEXT",self._context


