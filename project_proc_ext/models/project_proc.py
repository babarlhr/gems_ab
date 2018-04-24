from odoo import models, fields

class PurchaseProject(models.Model):
    _inherit = 'purchase.project'
    
    project_status = fields.Selection([
                                ('active', 'Active'),
                                ('cancelled', 'Cancelled'),
                                ('completed', 'Completed'),
                                ], string="Project Status")
    key_data = fields.Text('Key Data')
    project_tags = fields.Many2many('purchase.project.tags', string="Tags")
    
    
class PurchaseProjectTags(models.Model):
    _name = 'purchase.project.tags'
    _description = 'Project Tags'
    
    name = fields.Char('Name', required=True)