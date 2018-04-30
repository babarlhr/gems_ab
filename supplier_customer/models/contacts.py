from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    contact_cr = fields.Char('CR')
    regions_tag = fields.Many2many('res.partner.regions', string="Tags (Region)")
    customer = fields.Boolean(string='Is a Customer', default=False,
                               help="Check this box if this contact is a customer.")
    
class ResPartnerRegions(models.Model):
    _name = 'res.partner.regions'
    
    name = fields.Char('Name')