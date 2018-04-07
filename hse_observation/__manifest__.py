# -*- coding: utf-8 -*-
{
    "name": "HSE Observation",
    "version": "11.2018.03.29.1",
    "author": "Denero Team",
    "website": "https://www.deneroteam.com",
    "category": "Project",
    "depends": ['operating_unit', 'hr', 'mail', 'calendar'],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "datas/sequence.xml",
        "views/hse_observation_view.xml",
        "wizard/views/wiz_activity_view.xml",
    ],
    'demo': [
    ],
    'installable': True,
}
