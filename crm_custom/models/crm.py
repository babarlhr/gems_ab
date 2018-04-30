from odoo import models, fields, api

AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Low'),
    ('2', 'High'),
    ('3', 'Very High'),
    ('4', 'Very Very High'),
    ('5', 'Most High'),
]

class CRMLead(models.Model):
    _inherit = 'crm.lead'
    
    operating_unit_id = fields.Many2one('operating.unit', string="Operating Unit")
    probability_based_value = fields.Float(string="Probability Based Value", compute="_compute_probability_based_value")
    priority = fields.Selection(AVAILABLE_PRIORITIES, string='Priority', index=True, default=AVAILABLE_PRIORITIES[0][0])
    manager_incharge = fields.Many2one('res.users', string="Manager Incharge")
    
#     Attachments
    client_docs_id = fields.One2many('ir.attachment', 'crm_client_docs_id', string="Client Docs In")
    commercial_docs_id = fields.One2many('ir.attachment', 'crm_commercial_docs_id', string="Commerical In")
    technical_docs_id = fields.One2many('ir.attachment', 'crm_technical_docs_id', string="Technical Docs In")
    proposal_out_id = fields.One2many('ir.attachment', 'proposal_in_id', string="Proposal In")
    
#     Expected Contract
    prospective_client = fields.Many2one('res.partner', string="Prospective Client")
    expected_starte_date = fields.Date(string="Expected start date")
    expected_end_date = fields.Date(string="Expected end date")
    expected_contract_terms = fields.Selection([
                                        ('one_off', 'One Off'),
                                        ('auto_renewable', 'Auto Renewable'),
                                        ('potentially_renewable', 'Potentially Renewable'),
                                        ], string="Expected Contract Terms")
    expected_max_contract_value = fields.Float('Max contract value')
    max_tonnage = fields.Float('Max Tonnage')
    tolerance =  fields.Float('Tolerance')
    
    crm_line_ids = fields.One2many('crm.lead.line','crm_lead_id', string="Expected Contract")
    crm_contract_id = fields.One2many('crm.lead.contract', 'crm_contract_id', string="CRM Contract")
    contract_count = fields.Integer(string='Expect Contracts', compute='_compute_expect_contracts')
    
    def _compute_expect_contracts(self):
        self.contract_count = len(self.crm_contract_id)
    
    @api.multi
    def action_view_contracts(self):
        action = self.env.ref('crm_custom.action_crm_expected_contract').read()[0]
        crm_contracts = self.mapped('crm_contract_id')
        if len(crm_contracts) > 1:
            action['domain'] = [('id', 'in', crm_contracts.ids)]
        elif crm_contracts:
            action['views'] = [(self.env.ref('crm_custom.crm_expected_contract_view_form').id, 'form')]
            action['res_id'] = crm_contracts.id
        return action
        
    def _compute_probability_based_value(self):
        for lead in self:
            lead.probability_based_value = lead.planned_revenue * (lead.probability / 100)
            
class CRMLeadLine(models.Model):
    _name = 'crm.lead.line'
    _description = 'CRM Line'
    
    crm_lead_id = fields.Many2one('crm.lead', string="CRM Lead")
    division = fields.Char('Division')
    rev_type = fields.Char('Rev. Type')
    description = fields.Char('User Description')
    change_type = fields.Selection([
                                ('rate', 'Rate'),
                                ('fixed', 'Fixed'),
                                ], string="Change Type")
    service_class = fields.Selection([
                                    ('normal', 'Normal'),
                                    ('shutdown', 'Shutdown'),
                                    ], string="Service Class")
    rate = fields.Float('Rate')
    unit = fields.Many2one('product.uom', string="Unit")
    line_from = fields.Float('From')
    line_to = fields.Float('To')
    max_value = fields.Float('Max Value')
    max_qty = fields.Integer('Max Quantity')