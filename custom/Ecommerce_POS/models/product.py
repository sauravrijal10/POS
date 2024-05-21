# -*- coding: utf-8 -*-
from odoo import models, fields

# class Product(models.Model):
#     _name = 'custom.product'
#     _inherit = 'product.template'
class CustomProduct(models.Model):
    _name = 'custom.product'
    _inherits = {'product.template': 'product_template_id'}

    # Add your custom fields here
    # custom_field = fields.Char(string='Custom Field')
    custom_product_id = fields.Char(string='Custom Product ID')
    product_template_id = fields.Many2one('product.template', required=True, ondelete='cascade', string='Product Template')

    