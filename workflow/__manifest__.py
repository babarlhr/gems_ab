# -*- coding: utf-8 -*-

{
    'name': 'Workflow',
    'version': '1.0',
    'author' : 'Odoo Advantage',
    'website' : 'www.erp.odoo.ie',
    'summary': 'Adding workflow to contacts',
    'description': """
    """,
    'depends': ['base','hr','product'],
    'data': [
                'security/workflow_security.xml',
                'views/contacts.xml',
                'views/employee.xml',
#                 'views/product.xml',
            ],
    'installable': True,
}