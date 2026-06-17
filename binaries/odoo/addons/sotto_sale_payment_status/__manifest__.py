{
    'name': 'Payment Status In sale Order',
    "author": "Sottosoft Solution",
    'version': '14.0.1',
    "website": "",
    'category': 'Extra Tools',
    "support": "sottosoftsolution@gmail.com",
    'summary': 'sale Order Payment status,Payment status in sale order,Payment status',
    'description': """
        Get Better idea of your Payment status from the sale order.
    """,
    'images': ["static/description/img_1.png"],
    'depends': ['sale_management'],
    'data': [
        'security/sale_payment_status_group.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application':True,
    "price": 0,
    "currency": "EUR"
}   
