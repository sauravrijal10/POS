{
    'name':'Ecommerce_POS',
    'depends':['base','product','point_of_sale'],
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/user.xml',
        'views/product.xml',
        'views/report.xml',
        'views/sales_details.xml',
        'views/session.xml',
        'views/config.xml'
        # 'views/template.xml',
    ]
}