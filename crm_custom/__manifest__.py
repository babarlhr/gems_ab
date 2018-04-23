{
    'name' : 'CRM Customization',
    'author' : 'Odoo Advantage Ireland',
    'category' : 'crm',
    'website' : 'www.odoo.ie',
    'data' : [
            'security/ir.model.access.csv',
            'views/crm_view.xml',
            ],
    'depends' : ['crm','base','product'],
    'installable' : True,
}