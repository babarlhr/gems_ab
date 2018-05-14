{
    'name' : 'Procurement Custom',
    'author' : 'Odoo Advantage Ireland',
    'website' : 'erp.odoo.ie',
    'data' : [
            'security/security.xml',
            'views/procurement.xml',
            'views/rfq.xml',
        ],
    'depends' : ['purchase','capex_procurement'],
    'installable' : True,
}