# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{

    'name': 'Shopping List',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Emmanuel',
    'category': 'All',
    'summary': 'shopping_list',
    'description': """
        A module which will help to notify the users which items needs to be purchased recurrently and save the prices and locations records
    """,
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/budget.xml',
        'views/category.xml',
        'views/frequency.xml',
        'views/notification.xml',
        'views/one_time_purchase.xml',
        'views/payment.xml',
        'views/product.xml',
        'views/purchase_history.xml',
        'views/list.xml',
        'views/list_line.xml',
        'views/user.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
