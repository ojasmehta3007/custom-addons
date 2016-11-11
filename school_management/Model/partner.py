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

class partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    check_priority = fields.One2many('priority.table','select_name','Check Your Priorities:')

    # @api.multi
    # def write(self, vals):
    #     print "vals====================",vals
    #     a = self._context.get('params')['id']
    #     print "context===================",a
    #
    #     b = self.env['priority.table'].search(['&',('select_name','=',a),('set_priority','=','true')])
    #     print "#########################################",b.set_priority
    #     local = b.set_priority
    #     print "local==========================",local
    #
    #     return super(partner,self).write(vals)

