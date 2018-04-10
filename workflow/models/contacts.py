from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    state = fields.Selection([
                            ('unverified', 'Unverified'),
                            ('verified', 'Verified'),
                            ], readonly=True, copy=False, index=True, track_visibility='onchange', string="State", default='unverified')
    
    def verification(self):
        for rec in self:
            rec.state = 'verified'