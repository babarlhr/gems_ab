# -*- coding: utf-8 -*-
{
    "name": "Docs Control App",
    "version": "1.0",
    "author": "Odoo Advantage Ireland",
    "website": "www.odoo.ie",
    "category": "",
    "depends": ['hr','mail'],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/template.xml',
        'views/document_control_view.xml',
        'views/menus.xml',
        'datas/sequence.xml',
    ],
    'demo': [
    ],
    'installable': True,
}
