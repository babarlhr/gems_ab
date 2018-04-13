# -*- coding: utf-8 -*-

{
    'name': 'Hazmat App',
    'version': '1.0',
    'author' : 'Odoo Advantage Ireland',
    'website' : 'www.erp.odoo.ie',
    'summary': 'Hazmat Application',
    'description': """
    """,
    'depends': ['product', 'operating_unit', 'base'],
    'data': [
                'security/security.xml',
                'security/ir.model.access.csv',
                'datas/sequence.xml',
                'views/material.xml',
                'views/menu.xml',
            ],
    'installable': True,
}