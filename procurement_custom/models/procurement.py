from odoo import models, fields, api
from datetime import datetime

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    department_id = fields.Many2one('hr.department', string="Department")
    client_id = fields.Many2one('res.partner', string="Client Name")

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    date_planned = fields.Date(string='Scheduled Date', required=True, index=True)