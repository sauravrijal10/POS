{
    'name':'Ecommerce_POS',
    'depends':['base','product','point_of_sale','sale','stock'],
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/user.xml',
        'views/product.xml',
        'views/posconfig.xml',
        'views/order.xml',
        'views/report.xml',
         'wizard/sales_details.xml',
        # 'views/salesdetails.xml',
        # 'views/client.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'Ecommerce_POS/static/src/js/**/*',
            'Ecommerce_POS/static/src/xml/**/*',
        ],
    },
}
