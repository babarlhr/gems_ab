from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp

class MaterialAdmin(models.Model):
    _name = "material.admin"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _description = 'Material Admin'
    _rec_name = "name"
    
#     name = fields.Char('Name')
    name = fields.Char('Manifest Code', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    material_unit = fields.Many2one('product.uom', string="Material Unit")
    material_type = fields.Many2one('material.type', string="Material Type")
    quantity = fields.Float('Quantity')
    mass_conversion = fields.Float('Mass Conversion', compute="_compute_mass_conversion", digits=dp.get_precision('Mass Conversion'), store=True)
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
    classification = fields.Selection([
                        ('acid_w_w', 'Acid W/W'),
                        ('acid_sludge', 'Acid sludge'),
                        ('acids', 'Acids'),
                        ('alkyl_w_W', 'Alkyl W/W'),
                        ('amine_waste', 'Amine Waste'),
                        ('ammonia_w_w', 'Ammonia W/W'),
                        ('asbestos', 'Asbestos'),
                        ('batteries', 'Batteries'),
                        ('catalysts_etc', 'Catalysts etc'),
                        ('caustic_soda', 'Caustic Soda'),
                        ('chemical_sludge', 'Chemical Sludge'),
                        ('chemical_waste', 'Chemical Waste'),
                        ('chemical_w_w', 'Chemical W/W'),
                        ('chemicals', 'Chemicals'),
                        ('clay_waste', 'Clay Waste'),
                        ('diesel_w_w', 'Diesel W/W'),
                        ('drums_empty', 'Drums Empty'),
                        ('drums_full', 'Drums Full'),
                        ('fly_ash', 'Fly Ash'),
                        ('ibcs', 'IBCs'),
                        ('lime_waste', 'Lime Waste'),
                        ('oil_waste', 'Oil (Waste)'),
                        ('oily_sludge', 'Oily Sludge'),
                        ('oily_sludge_sol', 'Oily Sludge (Sol)'),
                        ('oily_w_w', 'Oily W/W'),
                        ('petrochemical_w_w', 'Petrochemical W/W'),
                        ('sewage', 'Sewage'),
                        ('soot_ash', 'Soot/Ash'),
                        ('spent_caustic_w_w', 'Spent Caustic W/W'),
                        ('sludge_to_landfill', 'Sludge to Landfill'),
                        ('solids_to_landfill', 'Solids to Landfill'),
                        ('sulphur_waste', 'Sulphur Waste'),
                        ('waste_to_landfill', 'Waste to Landfill'),
                    ])
    treatment_path = fields.Selection([
                        ('chemical', 'Chemical'),
                        ('asbestos', 'Asbestos'),
                        ('other', 'Other'),
                        ('catalyst', 'Catalyst'),
                        ('solids', 'Solids'),
                        ('oil', 'Oil'),
                        ('fly_ash_ash', 'Fly Ash/Ash'),
                        ('petrochemical', 'Petrochemical'),
                        ('sewage', 'Sewage'),
                        ('spent_caustic', 'Spent Caustic'),
                        ('landfill', 'Landfill'),
                    ], string="Treatment path", readonly=True, compute="_compute_field_val")
    market_size = fields.Selection([
                            ('market', 'Market'),
                            ('non_market', 'Non Market'),
                        ], string="Market size relative", readonly=True,  compute="_compute_field_val")
    
    @api.depends('classification')
    def _compute_field_val(self):
        for rec in self:
            for class_rec in self.env['classification.matrix'].search([]):
                if class_rec.classification == rec.classification:
                    rec.treatment_path = class_rec.treatment_path
                    rec.market_size = class_rec.market_size
        
    state = fields.Selection([
            ('draft', 'Material Admin'),
            ('wb_operator', 'WB Operator'),
            ('fingerprint_analysis', 'Fingerprint Analysis'),
            ('process_data', 'Process Data'),
            ('close', 'Close'),
        ], readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    
#     @api.multi
    @api.depends('quantity','material_unit')
    def _compute_mass_conversion(self):
        for rec in self:
            rec.mass_conversion = rec.material_unit.factor * rec.quantity
    
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
            
    @api.multi
    def state_to_close(self):
        for rec in self:
            rec.state = 'close'
            
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('material.admin') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('material.admin') or _('New')
        return super(MaterialAdmin, self).create(vals)

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
    