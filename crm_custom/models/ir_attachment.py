from odoo import models, fields

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    
    crm_client_docs_id = fields.Many2one('crm.lead')
    crm_commercial_docs_id = fields.Many2one('crm.lead')
    crm_technical_docs_id = fields.Many2one('crm.lead')
    proposal_in_id = fields.Many2one('crm.lead')