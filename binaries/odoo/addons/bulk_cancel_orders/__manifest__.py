# -*- coding: utf-8 -*-
{
    'name': 'Bulk cancel orders',
    'summary': 'Cancel sale orders in bulk',
    'description': 'Odoo addon to add the ability to cancel sale orders in bulk from the UI (quotation view)',

    'author': 'Mekom Solutions',
    'website': 'http://www.mekomsolutions.com',
    'support': 'ipredictitsolutions@gmail.com',

    'category': 'Sales',
    'version': '1.0.0-SNAPSHOT',
    'depends': ['sale_management'],

    'data': [
        'security/ir.model.access.csv',
        'wizard/bulk_cancel_orders.xml',
    ],

    'auto_install': True,
    'installable': True,
}
