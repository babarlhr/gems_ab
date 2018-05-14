from odoo import models, fields, api
from docutils.frontend import store_multiple

# class CustomerInoviceReport(models.Model):
#     _name = 'report.sale_invoice_custom.report_invoice_custom_arabic'
#     
#     @api.model
#     def get_report_values(self, docids, data=None): 
#         docargs = {} 
#         return docargs

# class AccountInovice(models.Model):
#     _inherit = 'account.invoice'
     
#     vat_amount = fields.Monetary(string="VAT", readonly=True, compute="_compute_vat_total")
#      
#     def _compute_vat_total(self):
#         round_curr1 = self.currency_id.round
#         self.vat_amount = sum(round_curr1(line.total_vat_lines) for line in self.invoice_line_ids)
        
#     @api.one
#     @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
#                  'currency_id', 'company_id', 'date_invoice', 'type')
#     def _compute_amount(self):
#         round_curr = self.currency_id.round
#         self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line_ids)
#         self.amount_tax = sum(round_curr(line.amount_total) for line in self.tax_line_ids)
#         
#         self.vat_amount = sum(round_curr(line.total_vat_lines) for line in self.invoice_line_ids)
#         self.amount_total = self.amount_untaxed + self.amount_tax + self.vat_amount
#         amount_total_company_signed = self.amount_total
#         amount_untaxed_signed = self.amount_untaxed
#         if self.currency_id and self.company_id and self.currency_id != self.company_id.currency_id:
#             currency_id = self.currency_id.with_context(date=self.date_invoice)
#             amount_total_company_signed = currency_id.compute(self.amount_total, self.company_id.currency_id)
#             amount_untaxed_signed = currency_id.compute(self.amount_untaxed, self.company_id.currency_id)
#         sign = self.type in ['in_refund', 'out_refund'] and -1 or 1
#         self.amount_total_company_signed = amount_total_company_signed * sign
#         self.amount_total_signed = self.amount_total * sign
#         self.amount_untaxed_signed = amount_untaxed_signed * sign
    
# class AccountInvoiceLine(models.Model):
#     _inherit = 'account.invoice.line'
#     
#     vat_percent = fields.Float('VAT(%)', store=True)
#     total_vat_lines = fields.Float('Total VAT', compute="_compute_vat_tax", store=True)
#     total_with_vat = fields.Monetary(string='Total', store=True, readonly=True, compute="_compute_vat_tax")
#     
#     @api.depends('vat_percent')
#     def _compute_vat_tax(self):
#         for rec in self:
#             rec.total_vat_lines = rec.price_subtotal * (rec.vat_percent / 100)
#             rec.total_with_vat = rec.total_vat_lines + rec.price_subtotal