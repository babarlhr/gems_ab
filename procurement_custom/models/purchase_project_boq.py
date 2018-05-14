from odoo import models, fields, api

class PurchaseProjectBoq(models.Model):
    _inherit = 'purchase.project.boq'
    
    state = fields.Selection([
            ('draft', 'New'),
            ('technical_approval', 'Technical Approval'),
            ('commercial_approval', 'Commercial Approval'),
            ('finance_approval', 'Finance Approval'),
            ('management_approval', 'management Approval'),
            ('done', 'Done'),
        ], string="State")
    
    technical_manager = fields.Many2one(
        'res.users', string='Technical approval by:', domain="[('share','=',False)]", required=False,
        
    )
    commersial_manager = fields.Many2one(
        'res.users', string='Commercial approval by:', domain="[('share','=',False)]", required=False
    )
    financial_manager = fields.Many2one(
        'res.users', string='Financial approval by:', domain="[('share','=',False)]", required=False
    )
    management_manager = fields.Many2one(
        'res.users', string='Management approval by:', domain="[('share','=',False)]", required=False
    )
    
    is_tec_manager = fields.Boolean()
    is_com_manager = fields.Boolean()
    is_fin_manager = fields.Boolean()
    is_mgt_manager = fields.Boolean()

    @api.multi
    def write(self, vals):
#         if 'state' in vals:
#             for rec in self:
#                 approval_type = False
#                 if rec.state == 'technical_approval':
#                     approval_type = 'Technical'
#                 elif rec.state == 'commercial_approval':
#                     approval_type = 'Commercial'
#                 elif rec.state == 'finance_approval':
#                     approval_type = 'Financial'
#                 elif rec.state == 'management_approval':
#                     approval_type = 'Management'
#                 model_id = self.env.ref('capex_procurement.model_purchase_project_boq').id
#                 try:
#                     activity_type_id = self.env.ref('mail.mail_activity_data_todo').id
#                 except ValueError:
#                     activity_type_id = False
#                 if approval_type:
#                     activity_ids = self.env['mail.activity'].search([
#                         ('project_approval', '=', approval_type),
#                         ('res_id', '=', rec.id),
#                         ('res_model_id', '=', model_id),
#                         ('activity_type_id', '=', activity_type_id)
#                     ])
#                     for activity_id in activity_ids:
#                         activity_id.action_feedback()
        return super(PurchaseProjectBoq, self).write(vals)