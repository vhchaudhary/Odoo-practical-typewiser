# -*- coding: utf-8 -*-

{
    # Module Info
    'name': 'Odoo case study',
    'version': '1.1',
    'category': '',
    'summary': 'Odoo case study typewiser',
    'description': """Odoo case study typewiser""",

    # Author
    'author': 'Vahta Chaudhary',
    'website': '',

    # Dependencies
    'depends': ['base', 'website'],

    # Data
    'data': [
        'security/ir.model.access.csv',
        'report/template.xml',
        'views/room_view.xml',
        'views/course_view.xml',
        'views/partner_view.xml',
        'wizard/course_report_view.xml',
        'views/template.xml',
        'views/website_menu_view.xml'
    ],
    'qweb': [
    ],

    # Technical Speci.
    'installable': True,
    'auto_install': False
}
