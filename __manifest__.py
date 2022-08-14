# -*- coding: utf-8 -*-
{
    'name': "edit_in_invoice_wood_art",

    'summary': "",

    'description': "",

    'author': "ahmed youssef ",
    'sequence': -100,

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],
    'application': 'Ture',

    # always loaded
    'data': [
        # 'report/report_action.xml',
        'report/report_tep_inv.xml',

        'views/views.xml',

        # report_action.xml
#
    ],
}
