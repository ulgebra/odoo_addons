# -*- coding: utf-8 -*-
{
    'name': "Twilio SMS",

    'summary': "Twilio SMS by Ulgebra",

    'description': "Long description of module's purpose",

    'author': "Ulgebra",

    'website': "https://sms.ulgebra.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'SMS and Whatsapp',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm', 'ulgebra-odoo'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/app_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

