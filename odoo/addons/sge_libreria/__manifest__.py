# -*- coding: utf-8 -*-
{
    'name': "Libreria",

    'summary': "Modulo de ejemplo SGE",

    'description': """
Modulo de ejemplo SGE<br/>
Gestion de una librería
    """,

    'author': "Soy yo",
    'website': "https://www.mipaginita.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/categoria.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

