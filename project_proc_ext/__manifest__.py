{
    'name' : 'Project Proc Ext',
    'description' : 'Adding some fields to project module',
    'version' : '1.0',
    'author' : 'Odoo Advantage Ireland',
    'website' : 'www.odoo.ie',
    'data' : [
            'security/ir.model.access.csv',
            'views/project_view.xml',
            ],
    'depends' : ['capex_procurement'],
    'installable' : True,
}