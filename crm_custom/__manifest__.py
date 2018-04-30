{
    'name' : 'CRM Customization',
    'author' : 'Odoo Advantage Ireland',
    'category' : 'crm',
    'website' : 'www.odoo.ie',
    'data' : [
            'security/ir.model.access.csv',
            'views/crm_view.xml',
            'views/expect_contract_view.xml'
            ],
    'depends' : ['crm','base','product','sale'],
    'installable' : True,
}