{
    'name' : 'Employee Custom',
    'description' : 'Adding fields to employee Form',
    'author' : 'Odoo IE',
    'website' : 'www.erp.odoo.ie',
    'depends' : ['hr', 'hr_gamification'],
    'data' : [
                "security/ir.model.access.csv",
                'views/employee_ext_view.xml',
            ],
    'installable' : True,
}