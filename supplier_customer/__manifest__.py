# -*- coding: utf-8 -*-
{
    "name": "Customer and Supplier",
    "version": "1.0",
    "author": "Odoo Advantage Ireland",
    "website": "www.odoo.ie",
    "category": "contacts",
    "depends": ['contacts', 'base','workflow'],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/contacts_menu.xml',
        'views/res_partner_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
}
