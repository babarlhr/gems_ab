from odoo import models, fields

class Applicant(models.Model):
    _inherit = "hr.applicant"
    
    source_id = fields.Char('Source')
    type_id = fields.Char('Educational Qualification')
    
    current_location = fields.Char("Current Location")
    years_of_exp = fields.Char("Years of Experience")
    languages = fields.Char('Languages')
    it_skills = fields.Char("IT Skills")
    nationalities = fields.Char("Nationalities")
    employeed = fields.Boolean("Employeed")
    employer = fields.Char("Employer / Last Employer")
    current_visa = fields.Char("Current Visa status")
    
    package = fields.Selection([
                                ('agreed', 'Agreed'),
                                ('non_agreed', 'Non Agreed'),
                                ])
    visa_country = fields.Selection([
                                    ('ksa' , 'KSA'),
                                    ('uae' , 'UAE'),
                                    ('india' , 'India'),
                                    ('spain' , 'Spain')
                                    ])
    visa_type = fields.Selection([
                                ('transferable_iqama' , 'Transferable Iqama'),
                                ('non_transferable_iqama' , 'NON Transferable Iqama'),
                                ('new_iqama' , 'New Iqama'),
                                ('work_visit_visa' , 'Work Visit Visa'),
                                ('business_visa' , 'Business Visa'),
                                ('visa_not_required' , 'Visa Not Required'),
                                ])
    familty_status = fields.Selection([
                                        ('single' , 'Single'),
                                        ('married' , 'Married'),
                                        ])
    dependents = fields.Integer("Dependents")
    accomodation = fields.Selection([
                                    ('sca' , 'Standard Company Allowance'),
                                    ('nsca' , 'Non Standard Company Allowance'),
                                    ('company_accomodation' , 'Comapny Accomodation'),
                                    ('not_provided' , 'Not Provided'),
                                    ])
    medical_insurance = fields.Selection([
                                        ('provided' , 'Provided'),
                                        ('not_provided' , 'Not Provided'),
                                        ])
    carrier = fields.Char('Carrier')
    policy_type = fields.Char("Policy Type")
    medical_history = fields.Text('Medical History')
    blood_type = fields.Char('Bood Type')
    next_to_kin = fields.Char('Next To Kin')
    transportation = fields.Selection([
                                        ('sca' , 'Standard Company Allowance'),
                                        ('sr' , 'Company Rental'),
                                        ('ct' , 'Company Transport'),
                                        ('soc' , 'Compony Owned Car'),
                                        ('not_provided' , 'Not Provided'),
                                    ])
    transportation_history = fields.Text('Transportation History')
    
#     Vacation group fields
    frequency = fields.Integer('Frequency')
    duration = fields.Integer('Duration (Days)')
    flights = fields.Selection([
                                ('individual' , 'Individual'),
                                ('family' , 'Family'),
                                ('not_provided' , 'Not Provided'),
                                ])
    number_of_tickets = fields.Integer('No: of Tickets(Per anuum)')
    phone = fields.Selection([
                            ('provided' , 'Provided'),
                            ('not_provided' , 'Not Provided'),
                            ])
    mob_spec = fields.Char('Spec')
    plan = fields.Char('Plan')
    computer = fields.Selection([
                                ('provided' , 'Provided'),
                                ('not_provided' , 'Not Provided'),
                                ])
    computer_spec = fields.Char('Spec')
    
#     Software group fields
    office_lic_type = fields.Char('Office 365 Lic. Type')
    ms_project_type = fields.Char('Ms Project Type')
    ms_visio_type = fields.Char('Ms Visio Type')
    tresorit = fields.Char('Tresorit')
    odoo = fields.Char('Odoo')
    cms_candy_type = fields.Char('CMS Candy Type')
    fms_type = fields.Char('FMS Type')
    
#     Recruit details group fields
    visa_type_recruit = fields.Char('Visa Type')
    visa_number = fields.Char('Visa Number')
    interim_AT = fields.Char('Interim Accomodation Type')
    final_AT = fields.Char('Final Accomodation Type')
    interim_transport = fields.Char('Interim Transport')
    final_transport = fields.Char('Final Transport')
    arrival_date = fields.Date('Arrival Date')
    travel_arrangements = fields.Char('Travel Arrangements')
    onboarding_manager = fields.Many2one('hr.employee', 'Onboarding Manager')
    line_manager = fields.Many2one('hr.employee', 'Line Manager')
    status_incharge_manager = fields.Selection([
                                                ('pending' , 'Pending'),
                                                ('onboarding' , 'Ready for onboarding'),
                                                ])
    approved_job_offer = fields.Selection([
                                            ('yes' , 'Yes'),
                                            ('no' , 'No'),
                                        ], 'Approved for Job Offer')
    approved_by = fields.Many2one('hr.employee', 'Approved By')
    approval_date = fields.Date('Date')
    
    approved_by_chairman = fields.Char('Approved By Chairman')
    chairman_approval_date = fields.Date('Approval Date')