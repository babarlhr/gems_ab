from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    contact_cr = fields.Char('CR')