# -*- coding: utf-8 -*-
{
    'name': "theme_penquin",

    'summary': """
        Penguin Website""",

    'description': """
        Penguin Theme
    """,

    'author': "Shore Point System Private Limited",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Theme',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/snippets.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}