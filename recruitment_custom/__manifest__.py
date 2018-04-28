{
    'name' : 'Recruitment Custom',
    'description' : 'Adding fields to recruitment module',
    'author' : 'Odoo Advantage Ireland',
    'website' : 'www.erp.odoo.ie',
    'depends' : ['hr', 'hr_recruitment','catalyst_hrms_operating_unit'],
    'data' : [
                'views/job_position.xml',
                'reports/job_position_reports.xml',
                'reports/job_position_template.xml',
                'views/applications.xml',
            ],
    'installable' : True,
}