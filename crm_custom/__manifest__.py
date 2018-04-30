{
    'name' : 'CRM Customization',
    'author' : 'Odoo Advantage Ireland',
    'category' : 'crm',
    'website' : 'www.odoo.ie',
    'data' : [
            'security/ir.model.access.csv',
            'views/expect_contract_view.xml',
            'views/crm_view.xml',
            ],
    'depends' : ['crm','base','product','sale_stock'],
    'installable' : True,
}