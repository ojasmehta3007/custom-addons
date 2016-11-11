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
from openerp.osv import fields, osv, expression  # V7
from openerp import models, fields, api, _  # v8
from openerp.exceptions import except_orm, UserError, ValidationError

import re
import time
import datetime
from datetime import datetime
from time import gmtime, strftime


class vetclinic_animal(models.Model):
    _name = 'vetclinic.animal'

    name = fields.Char('Name:', size=34)
    birthdate = fields.Date('BirthDate:')
    classification_id = fields.Many2one('vetclinic.classification','Classification:')
    breed_id = fields.Many2one('vetclinic.breed','Breed:')
    labels_ids = fields.Many2many('vetclinic.labels','rel_animal_labels','animal_id','labels_id',string='Labels:')
    history = fields.Text('History :')
    res_partner_id = fields.Many2one('res.partner','Owner:')
    animalvaccinations_id = fields.One2many('vetclinic.animalvaccination','animal_id','Vaccinations:')
    animal_breed = fields.One2many('vetclinic.breed','classification_id_of_breed','EXECUTE')


    @api.multi
    def myfunction(self):
        print "==========================",self._context
        animal_id = self._context.get('params')['id']
        print "b================",animal_id
        # a = self._context.get('params')['id']
        # print "a=====================",a


        # ac = self.env['ir.model.data'].xmlid_to_res_id('boatcompany.vetclinic_animal_form', raise_if_not_found=True)
        # ac = self.env['']
        # v_a = False
        # for o in self:
        #     v_a = o.id
        result = {
                    'name': '2nd Animal',
                    'view_type': 'form',
                    'res_model': 'vetclinic.classification',
                    'context': {'default_name': animal_id},
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form'
                }
        return result













class vetclinic_animalvaccination(models.Model):
    _name = 'vetclinic.animalvaccination'

    products_id = fields.Many2one('product.product','Vaccination:')
    duedate = fields.Date('Due Date:')
    dateperfomed = fields.Date('Date Performed:')
    animal_id = fields.Many2one('vetclinic.animal','Animal:')


class vetclinic_res_partner(models.Model):
    _inherit = 'res.partner'

    animal_ids = fields.One2many('vetclinic.animal','res_partner_id',string='Pets:')



class vetclinic_classification(models.Model):
    _name = 'vetclinic.classification'

    name = fields.Char('Name:')
    breed_id = fields.One2many('vetclinic.breed','classification_id_of_breed','Breeds :')
    image_id = fields.Many2one('vetclinic.images','Choose Your Image:')
    display_image = fields.Binary(related='image_id.image')
    # vacc_class = fields.One2many('vetclinic.images','image_id','EXECUTE',related='image_id.image')



    @api.multi
    def Pass(self):
        print "Button is Pressed=============================="
    # @api.multi
    # @api.onchange('image_id')
    # def myfunction(self):
    #     print "Self is printing==========================================",self.image_id
    #     for each in self.image_id:
    #         print "each====================================",each.name
    #         inv = self.env['vetclinic.images'].browse(each.id)
    #         print "inv is printing=====================================",inv.name
    #         self.write({
    #             'display_image' : inv.image
    #         })
            # print "Name is working==========================",inv.name
            # print "Image is working==========================",inv.image


                # print "Inside For=========================",each.name
                # a = each.image


                # code here





class vetclinic_breed(models.Model):
    _name = 'vetclinic.breed'

    name = fields.Char('Name:', size=34)
    classification_id_of_breed = fields.Many2one('vetclinic.classification','Classification')
    animal_o2m = fields.One2many('vetclinic.animalvaccination','animal_id','EXECUTE THIS')




class vetclinic_labels(models.Model):
    _name = 'vetclinic.labels'

    name = fields.Char('Name:', size=34)


class vetclinic_images(models.Model):
    _name = 'vetclinic.images'


    name = fields.Char('Name:')
    image = fields.Binary('Image :')

