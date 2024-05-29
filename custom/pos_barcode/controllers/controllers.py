# -*- coding: utf-8 -*-
# from odoo import http


# class PosBarcode(http.Controller):
#     @http.route('/pos_barcode/pos_barcode', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_barcode/pos_barcode/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_barcode.listing', {
#             'root': '/pos_barcode/pos_barcode',
#             'objects': http.request.env['pos_barcode.pos_barcode'].search([]),
#         })

#     @http.route('/pos_barcode/pos_barcode/objects/<model("pos_barcode.pos_barcode"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_barcode.object', {
#             'object': obj
#         })
