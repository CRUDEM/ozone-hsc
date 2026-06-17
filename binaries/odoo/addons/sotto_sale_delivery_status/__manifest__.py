{
    'name': 'Sale Order Delivery Status',
    "author": "Sottosoft Solution",
    'version': '14.0.1',
    "website": "",
    'category': 'Extra Tools',
    "support": "sottosoftsolution@gmail.com",
    'summary': 'sale Order Delivery status,Delivery status in sale order,Order status',
    'description': """
        Get Better idea of your delivery status from the sale order.
    """,
    'images': ["static/description/img_1.png"],
    'depends': ['sale_management','stock'],
    'data': [
        'security/sale_delivery_status_group.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application':True,
    "price": 0,
    "currency": "EUR"
}   
