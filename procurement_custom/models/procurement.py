from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    department_id = fields.Many2one('hr.department', string="Department")
    client_id = fields.Many2one('res.partner', string="Client Name")
#     project_custom_id = fields.Many2one('project.project', string="Project")