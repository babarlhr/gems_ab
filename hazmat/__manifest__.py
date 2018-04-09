# -*- coding: utf-8 -*-

{
    'name': 'Hazmat App',
    'version': '1.0',
    'author' : 'Odoo IE',
    'website' : 'www.erp.odoo.ie',
    'summary': 'Hazmat Application',
    'description': """
    """,
    'depends': ['product', 'operating_unit', 'base'],
    'data': [
                'views/material.xml',
                'views/menu.xml',
            ],
    'installable': True,
}