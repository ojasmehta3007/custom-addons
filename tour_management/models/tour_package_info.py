from openerp import models, fields, api, _
from openerp.exceptions import ValidationError
from datetime import datetime
import pytz
from openerp import SUPERUSER_ID

class tour_package_info(models.Model):

    # _name='tour.package.info'
    _inherit='product.template'

    tour_type = fields.Selection({('National','Domestic'),('International','International')})
    tour_code = fields.Char('Tour Code', readonly=True)
    start_date = fields.Date('Start Date')
    no_of_nights = fields.Float('No of Night')
    state = fields.Selection({('start','Query'),('confirm','Confirmed'),('cancel','Cancelled')})
    itenary = fields.One2many('package.itenary','itenary_id',string="Package Itenary")
    hotel = fields.Many2many('hotel.detail')
    note = fields.Text(string="Tour Note")

    @api.model
    def create(self, vals):
        print "===============ir.sequence",self.env['ir.sequence']

        sequence_val = self.env['ir.sequence'].get('Tour code')
        print "========================",sequence_val
        vals.update({'tour_code':str(sequence_val)})
        res = super(tour_package_info,self).create(vals)
        return res

class customer_detail(models.Model):

    _inherit='res.partner'

    is_member = fields.Boolean()
    gender = fields.Selection([('Male','Male'),('Female','Female')])
    user_id = fields.Char()
    password = fields.Char()

class package_intenery(models.Model):

    _name='package.itenary'

    itenary_id = fields.Many2one('product.template')
    day = fields.Integer('Day')
    itenary = fields.Text('Itenary')
    night_hold = fields.Many2one('city.detail',string="Night Hold")
    hotel_detail = fields.Many2one('hotel.detail')

class tour_management_hotel(models.Model):

    _name='hotel.detail'

    name=fields.Char('Hotel Name')
    image=fields.Binary('Image')
    state_id = fields.Many2one('res.country.state',string="State")
    city_id = fields.Many2many('city.detail',string = 'City')
    priority = fields.Selection([('0','0 star'),('1','1 star'),('2','2 star'),
                                 ('3','3 star'),('4','4 star'),('5','5 star'),
                                 ('6','6 star'),('7','7 star')])
    phone = fields.Char(string = 'Phone')
    email = fields.Char(string = 'Email')
    fax = fields.Char(string = 'Fax')
    inclusive = fields.One2many('meal.detail','inclusive_id',string='Meal')
    facility = fields.Many2many('hotel.facility','facility_id',string="Facility")
    vendor_name = fields.Many2one('vendor.detail.info',string="Vendor")
    vendor_phone = fields.Char(related="vendor_name.phone", string="Vendor Phone")

class meal_plan(models.Model):

    _name='meal.detail'

    inclusive_id = fields.Many2one('hotel.detail')
    meal = fields.Selection({('0','Breakfast'),('1','Lunch'),('2','Dinner')})
    rate = fields.Float('Rate')

class hotel_facilities(models.Model):

    _name='hotel.facility'

    name = fields.Char('Facility')

class city_detail(models.Model):

    _name='city.detail'

    name = fields.Char("City")
    city_code = fields.Integer("Zip Code")
    state = fields.Many2one('res.country.state',String="State")
    country = fields.Many2one('res.country',String="Country")

    # country = fields.Many2one('res.country', 'Country')
    # state=fields.Many2one(related='country.state.id', store=True)

    @api.multi
    def name_get(self):
        context = dict(self._context)
        if context.has_key('default_state_id'):
            res = []
            for value in self.search([]):
                if value.state.name == self.env['res.country.state'].browse(context['default_state_id']).name:
                    res.append([value.id, "%s: %s" % (value.state.name, value.name)])
            return res
        else:
            return super(city_detail,self).name_get()