{
    'name' : 'Procurement Custom',
    'author' : 'Odoo Advantage Ireland',
    'website' : 'erp.odoo.ie',
    'data' : [
            'views/procurement.xml',
            'security/security.xml',
        ],
    'depends' : ['purchase','base','project','capex_procurement'],
    'installable' : True,
}