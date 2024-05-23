# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CustomProduct(models.Model):
    _name = 'custom.product'
    _inherits = {'product.template': 'product_template_id'}

    product_template_id = fields.Many2one('product.template', required=True, ondelete='cascade', string='Product Template')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_product_id = fields.Char(string='Custom Product ID')


