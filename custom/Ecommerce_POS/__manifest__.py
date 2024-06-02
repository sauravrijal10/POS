{
    'name':'Ecommerce_POS',
    'depends':['base','product','point_of_sale','stock_account','sale','web'],
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/user.xml',
        'views/product.xml',
        'views/posconfig.xml',
        'views/order.xml',
        'views/inventory.xml',
        'views/error_template.xml',
        'views/create_user_view.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'Ecommerce/static/src/js/create_user.js',
        ],
    },
    'installable': True,
    'application': True,
}