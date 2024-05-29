{
    'name': 'Ecommerce_POS',
    'depends': ['Ecommerce_POS', 'product','point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/user.xml',
        'views/product.xml',
        'views/order.xml',
        'views/pos_config_view.xml',
        
    ],
   

    'installable': True,
    'auto_install': False,
    'application': True,
}
