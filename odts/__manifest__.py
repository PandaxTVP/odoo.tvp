# -*- coding: utf-8 -*-
{
    'name': "Mi Primer Modulo",

    'summary': """
        Creacion del Primer Modulo""",

    'description': """
        Este es el ejemplo de la creacion de un modulo desde 0
    """,

    'author': "Pandax",
    'website': "www.gtvp.odoo.com",
    'category': 'Modulo Automotriz',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}