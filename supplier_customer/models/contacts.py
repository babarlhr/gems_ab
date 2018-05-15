from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    contact_cr = fields.Char('CR')
    regions_tag = fields.Many2many('res.partner.regions', string="Tags (Region)")
    customer = fields.Boolean(string='Is a Customer', default=False,
                               help="Check this box if this contact is a customer.")
    longitude = fields.Char('Longitude')
    latitude = fields.Char('Latitude')
    google_address = fields.Char('Google Map Address')
    street3 = fields.Char('Address')
    
class ResPartnerRegions(models.Model):
    _name = 'res.partner.regions'
    
    name = fields.Char('Name')