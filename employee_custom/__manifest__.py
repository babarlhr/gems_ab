{
    'name' : 'Employee Custom',
    'description' : 'Adding fields to employee Form',
    'author' : 'Odoo Advantage Ireland',
    'website' : 'www.erp.odoo.ie',
    'depends' : ['hr', 'hr_gamification','mail'],
    'data' : [
                "security/ir.model.access.csv",
                'views/employee_ext_view.xml',
            ],
    'installable' : True,
}