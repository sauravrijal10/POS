# -*- coding: utf-8 -*-
# from odoo import http


# class PosProduct(http.Controller):
#     @http.route('/pos_product/pos_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_product/pos_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_product.listing', {
#             'root': '/pos_product/pos_product',
#             'objects': http.request.env['pos_product.pos_product'].search([]),
#         })

#     @http.route('/pos_product/pos_product/objects/<model("pos_product.pos_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_product.object', {
#             'object': obj
#         })
