# -*- coding: utf-8 -*-
{
    'name': "train_transportation",

    'summary': "Exercise Bootcamp Odoo Technical",

    'description': """
Long description of module's purpose
    """,

    'author': "Rimba",
    'website': "https://rimbashr.my.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/train_city_view.xml',
        'views/train_station_view.xml',
        'views/train_train_view.xml',
        # 'views/menuitem_views.xml',
        # 'wizard/train_schedule_wizard.xml',
        
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

