from openerp import models, fields, api, _
from openerp.exceptions import ValidationError
from datetime import datetime

class vender_detail_info(models.Model):
    _name = 'vendor.detail.info'

    name = fields.Char("Vendor Name")
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    location = fields.Many2one('city.detail', string="City/Location")

class passenger_detail(models.Model):
    _name = 'passenger.detail.info'

    travel_id1 = fields.Many2one('tour.query.detail')
    travel_id2 = fields.Many2one('tour.query.detail')
    travel_id3 = fields.Many2one('tour.query.detail')
    travel_id4 = fields.Many2one('tour.query.detail')
    travel_id5 = fields.Many2one('tour.query.detail')
    name = fields.Char("Passenger Name")
    age = fields.Integer('Age')
    gen = fields.Selection({('male','Male'),('female','Female')})

class tour_query(models.Model):

    _name='tour.query.detail'

    sequence =fields.Char(readonly=True)
    name = fields.Many2one('res.partner', string="Partner")
    email = fields.Char(related='name.email',string="Email")
    phone = fields.Char(related='name.phone',string="Phone")
    tour = fields.Many2one('product.template', string="Tour Name")
    date = fields.Datetime(default=datetime.now(), String="Date")
    ticket = fields.Boolean("Tickets")

    # fields for the member detail=================================
    adult_no = fields.Integer("No of Adults")
    adult= fields.One2many('passenger.detail.info','travel_id1', string="Info")
    extra_adult_no = fields.Integer("No of Exta Adults")
    extra_adult = fields.One2many('passenger.detail.info','travel_id2', string="Info")
    child_w_bed_no = fields.Integer('Child with Bed')
    child_w_bed = fields.One2many('passenger.detail.info','travel_id3', string="Info")
    child_w_nobed_no = fields.Integer('Child with no Bed')
    child_w_nobed = fields.One2many('passenger.detail.info','travel_id4', string="Info")
    infant_no = fields.Integer("No of Infants")
    infant = fields.One2many('passenger.detail.info','travel_id5', string="Info")

    # no_seats = fields.Integer(compute='_get_total',string="Total Seats")#this will call when we will change the field id depends is given then it will reflect
    no_seats = fields.Integer(string="Total Seats")#this will call when we will change the field then it will reflect

    #fields for vendor details
    vendor = fields.Many2one('vendor.detail.info', string="Vendor details")
    email1 = fields.Char(related="vendor.email", string="email", readonly='True')
    phone1 = fields.Char(related="vendor.phone", string="Phone", readonly='True')

    @api.model
    def create(self, vals):
        print "===============ir.sequence",self.env['ir.sequence']

        sequence_val = self.env['ir.sequence'].get('Query code')
        print "========================",sequence_val
        vals.update({'sequence':str(sequence_val)})
        res = super(tour_query,self).create(vals)
        return res

    @api.onchange('tour')
    def onchange_tour(self):
        print "========================",self
        tour_detail = self.env['hotel.detail'].search([])
        print "===================  val hotel ",tour_detail
        return tour_detail

    @api.onchange('adult_no','extra_adult_no' ,'infant_no' ,'child_w_bed_no' ,'child_w_nobed_no')
    def onchange_total(self):
        self.no_seats = self.adult_no + self.extra_adult_no + self.infant_no + self.child_w_bed_no + self.child_w_nobed_no

    @api.onchange('adult_no')
    def onchange_adult(self):
        pass_obj=self.env['passenger.detail.info']
        vals={'name':'','age':0,'gen':''}
        pass_obj.write(vals)
        result=[]
        for i in range(0,self.adult_no):
            result.append((0,0,vals))
            print "----------",vals
        self.adult = result

    @api.onchange('child_w_bed_no')
    def onchange_child_with_bed(self):
        pass_obj=self.env['passenger.detail.info']
        vals={'name':'','age':0,'gen':''}
        pass_obj.write(vals)
        result1=[]
        for i in range(0,self.child_w_bed_no):
            result1.append((0,0,vals))
        self.child_w_bed = result1

    @api.onchange('child_w_nobed_no')
    def onchange_child_with_no_bed(self):
        pass_obj=self.env['passenger.detail.info']
        vals={'name':'','age':0,'gen':''}
        pass_obj.write(vals)
        result2=[]
        for i in range(0,self.child_w_nobed_no):
            result2.append((0,0,vals))
        self.child_w_nobed = result2

    @api.onchange('extra_adult_no')
    def onchange_extra_adult(self):
        pass_obj=self.env['passenger.detail.info']
        vals={'name':'','age':0,'gen':''}
        pass_obj.write(vals)
        result3=[]
        for i in range(0,self.extra_adult_no):
            result3.append((0,0,vals))
        self.extra_adult = result3

    @api.onchange('infant_no')
    def onchange_infant(self):
        pass_obj=self.env['passenger.detail.info']
        vals={'name':'','age':0,'gen':''}
        pass_obj.write(vals)
        result4=[]
        for i in range(0,self.infant_no):
            result4.append((0,0,vals))
        self.infant = result4