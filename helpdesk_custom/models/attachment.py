from odoo import models, fields, api

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    
    helpdesk_ticket_ids = fields.Many2one('helpdesk.ticket', string="Helpdesk Tickets")