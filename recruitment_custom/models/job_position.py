from odoo import models, fields

class Job(models.Model):
    _inherit = "hr.job"
    
    reporting_manager = fields.Many2one('hr.employee', 'Reporting Manager')
    assign_location = fields.Char('Assignment Location')
    years_experience = fields.Char('Years of Experience')
    edu_qualification = fields.Char('Educational Qualification')
    languages = fields.Many2many('res.lang', 'job_position_language_rel', 'job_id', 'lang_id', string='Languages')
    it_skills = fields.Char('IT Skills')
    nationalities = fields.Char('Nationality')