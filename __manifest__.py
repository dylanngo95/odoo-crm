# -*- coding: utf-8 -*-
{
    'name': "Courts CRM",

    'summary': "Courts CRM Module",

    'description': """
This module will include customer service and loyalty service
    """,

    'author': "Courts Singapore",
    'website': "https://www.courts.com.sg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'crm',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/customer_point.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

