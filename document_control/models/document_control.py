from odoo import models, fields, api

class TravelApp(models.Model):
    _name="document.control"
    _rec_name="name"
    
    name = fields.Char('Name')