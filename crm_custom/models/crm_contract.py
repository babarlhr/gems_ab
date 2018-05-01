from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    exp_contract_id = fields.One2many('crm.lead.contract', 'sale_contract_id', string="CRM Contract")
    count_contract = fields.Integer(compute="_count_contracts")
    
    def _count_contracts(self):
        self.count_contract = len(self.exp_contract_id)

    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)
        if result.opportunity_id.crm_contract_id:
            result['exp_contract_id'] = result.opportunity_id.crm_contract_id
        return result

class CRMLeadContract(models.Model):
    _name = 'crm.lead.contract'
    _description = 'CRM Line'
    _rec_name = 'name'
    
    name = fields.Char(string="Name")
    crm_contract_id = fields.Many2one('crm.lead', string="CRM Lead")
    sale_contract_id = fields.Many2one('sale.order', string="Sale Order")
    
    contract_line_ids = fields.One2many('expected.contract.line', 'expected_contract_id', string="Contract Line")
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

class ExpectedContractLine(models.Model):
    _name = 'expected.contract.line'
    
    expected_contract_id = fields.Many2one('crm.lead.contract', string="Expected Contract")
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