# -*- coding: utf-8 -*-

{
    'name': 'RRSS Control Manager',
    'description': 'Manager Social Media',
    'author': 'In henry Vivas',
    'depends': ['base','product','project'],
    'application': False,
    'data': [
        'security/ir.model.access.csv',
        'views/control_post_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}