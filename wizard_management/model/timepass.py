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
import base64
from zipfile import ZipFile

import openerp
import urllib

from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8
from openerp.exceptions import except_orm,UserError, ValidationError




class timepass(models.Model):
    _name = 'timepass'

    name = fields.Binary('Name:')
    models_id = fields.Many2one('ir.model','Search From Models:')



    # @api.multi
    # def download(self):
    #     return {
    #             'type': 'ir.actions.act_url',
    #             'url': '/web/binary/download_document?model=ir.attachment&field=datas&id=%s&filename=%s&download=true' %(self.id),
    #             'target': 'self',
    #     }
    #



    # @api.multi
    # def download(self):
    #     url = "http://samarth32.blogspot.in/"
    #     # values = {'q':'java'}
    #     # data = urllib.urlencode(values)
    #     # data = data.encode('utf-8')
    #     req = urllib.urlopen(url)
    #     print "File Done"
    #     return {
    #         'res_model': 'ir.actions.act_url',
    #         'type': 'ir.actions.act_url',
    #         'target' : 'new',
    #         'url' : req,
    #     }

        # req = requests.Request(url,data)
        # resp = requests.urlopen(req)
        # respData = resp.read()
        # print "File Done"


        # print ("downloading with urllib")
        # return urllib.urlretrieve(url,"myimage.png")

        # r = requests.get("https://google.com")

        # url = "https://google.com/"
        # print ("File Reading Done...!!!!")
        # return{
        #     'res_model': 'ir.actions.act_url',
        #     'type': 'ir.actions.act_url',
        #     'target' : 'new',
        #     'url' : r,
        # }



    @api.multi
    def download(self):
        context = dict(self._context or {})
        # print 'hello'
        # active_ids = context.get('active_ids', False)
        a = self.models_id
        b = ""
        c = ""
        print "a++++++++++++++++++++++++",a
        print "Name+++++++++++++++++++++",a.name
        res = self.env['ir.attachment'].search([('res_model','=',self.models_id.model)])
        # for each in res:
        #     # url = '/web/content?model=ir.attachment&field=datas&id=%s&filename=%s&download=true' % (each.id,each.name)
        #     b = each.id
        #     c = each.name
        #     print each.id
        #     print each.name

        with ZipFile('/home/bista/Downloads/all-attachments.zip', 'w') as myzip:
            for each in res:
                file_datas = base64.b64decode(each.datas)
                each_file = open(each.name, "w")
                each_file.write(file_datas)
                each_file.close()
                # print file.name
                myzip.write(str(each_file.name))
            file_open = open('/home/bista/Downloads/all-attachments.zip', "rb+")
            encode_zip = base64.encodestring(file_open.read())
            id = self.create({'name': encode_zip})
            b = id.id
            c = id.name
            print "id================",id
            print "Name===========",id.name

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content?model=timepass&field=%s&id=%s&filename=all-attachments.zip&download=true' % (c,b) ,
            'target': 'self',
            }










        # c = self.env['ir.attachment'].search([('name','=','activity_graph_2012')])
        # print "c++++++++++++",c
        # for each in c:
        #     print str(each)


        # print "context++++++++++++++++++",self._context

        # for each in active_ids:
        #     each = self.env['ir.model'].browse(active_ids)
        #     print ('Done')
        #     print each.datas
        #     return each.datas
        #
