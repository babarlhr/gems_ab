from odoo import models, fields, api

class MaterialAdmin(models.Model):
    _name = "material.admin"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _rec_name = "name"
    
#     name = fields.Char('Name')
    name = fields.Char('Manifest Code')
    material_unit = fields.Many2one('product.uom', string="Material Unit")
    material_type = fields.Many2one('material.type', string="Material Type")
    quantity = fields.Float('Quantity')
    operating_unit = fields.Many2one('operating.unit', string="Operating Unit")
    client = fields.Many2one('res.partner', string="Client")
    
#     From client
    datetime_out = fields.Datetime('Date Time Out')
    
#     At site
    site_datetime_in = fields.Datetime('Date Time In')
    site_datetime_out = fields.Datetime('Date Time out (Site)')
    diver_name = fields.Many2one('hr.employee', string="Driver Name")
    iqama_no = fields.Char('Iqama No')
    sponsor_name = fields.Many2one('res.partner', string="Sponsor")
    truck_no = fields.Char('Truck #')
    iso_no = fields.Char('ISO #')
    transfer_slip_no = fields.Char('Transfer Slip No')
    site_material_desc = fields.Text('Description')
    
#     WB Operator
    client_wb_no = fields.Char('Client WB No:')
    client_wb_weight = fields.Float('Client WB Weight (KG)')
    wb_operator = fields.Many2one('hr.employee', string="WB Operator")
    gross_weight = fields.Float('Gross Weight')
    log_line_gw = fields.Datetime('Log Time (GW)')
    tear_weight = fields.Float('Tear Weight')
    log_time_tw = fields.Datetime('Log Time (TW)')
    net_weight = fields.Float('Net Weight')
    wb_slip_id = fields.One2many('ir.attachment','material_admin_id', string='WB Slip')
    
#     Fingerprint Analysis
    lab_technician = fields.Many2one('hr.employee', string="Lab Technician")
    density = fields.Float('Density')
    flast_point = fields.Float('Flast Point (*C)')
    ph = fields.Float('pH')
    appearance = fields.Char('Appearance')
    oil_presence = fields.Selection([
                                    ('yes', 'Yes'),
                                    ('no', 'No'),
                                    ], string="Oil Presence")
    h2s_presence = fields.Selection([
                                    ('yes', 'Yes'),
                                    ('no', 'No'),
                                    ], string="H2S Presence")
    
#     Process Data
    process_tech_name = fields.Many2one('hr.employee', string="Process Tech Name")
    approved_method_statment = fields.Selection([
                                                ('yes', 'Yes'),
                                                ('no', 'No'),
                                                ])
    method_statment_ref = fields.Char('Method Statment Reference')
    offloading_point = fields.Integer('Offloading Point')
    onloading_point = fields.Integer('Onloading Point')
    oil_recovery = fields.Float('Oil Recovery (%)')
    oil_recovery_tons = fields.Float('Oil Recovery (tons)')
    water = fields.Float('Water (%)')
    water_tons = fields.Float('Water (tons)')
    solids = fields.Float('Solids (%)')
    solids_tons = fields.Float('Solids (tons)')
    
    state = fields.Selection([
            ('draft', 'Material Admin'),
            ('wb_operator', 'WB Operator'),
            ('fingerprint_analysis', 'Fingerprint Analysis'),
            ('process_data', 'Process Data'),
        ], readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    
    @api.multi
    def state_to_wb_operator(self):
        for rec in self:
            rec.state = 'wb_operator'
            
    @api.multi
    def state_to_fingerprint_analysis(self):
        for rec in self:
            rec.state = 'fingerprint_analysis'
            
    @api.multi
    def state_to_process_data(self):
        for rec in self:
            rec.state = 'process_data'

class CompositeAnalysis(models.Model):
    _name = 'composite.analysis'
    _rec_name = "composite_id"
    
    composite_id = fields.Char('Composite ID', placeholder="Unique Composite ID")
    manifest_no = fields.Char('Manifest No')
    created_by = fields.Many2one('res.users', string="Created By", default=lambda self: self.env.user.id, readonly=True)
    date_time = fields.Datetime('Datetime')
    cod_ms_l = fields.Float('COD (mg/l)')
    tss_mg_l = fields.Float('TSS (ms/l)')
    composition_oil = fields.Float('Composition Oil (%)')
    composition_water = fields.Float('Composition Water (%)')
    composition_solids = fields.Float('Composition Solids/Sludge (%)')
    density = fields.Float('Density (g/ml)')
    
class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    material_admin_id = fields.Many2one('material.admin', string="Material Admin")
    
class MaterialType(models.Model):
    _name = "material.type"
    _rec_name = 'name'
    
    name = fields.Char('Name')