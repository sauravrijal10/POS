# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CustomProduct(models.Model):
    _name = 'custom.product'
    _inherits = {'product.template': 'product_template_id'}

    product_template_id = fields.Many2one('product.template', required=True, ondelete='cascade', string='Product Template')

    @api.model
    def action_open_label_layout(self):
        # Your code for the action here
        pass

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_product_id = fields.Char(string='Custom Product ID')


""" class CustomProduct(models.Model):
    _name = 'custom.product'

    _inherits = {'product.template': 'product_template_id'}

    custom_product_id = fields.Char(string='Custom Product ID')
    product_template_id = fields.Many2one('product.template', required=True, ondelete='cascade', string='Product Template')

    @api.model
    def action_open_label_layout(self):
        # Your code for the action here
        pass
    @api.model
    def custom_action(self):
        # Add your action logic here
        pass """

""" def fields_get(self, fields=None):
        result = super(CustomProduct, self).fields_get(fields=fields)
        if 'default_code' in result:
            result['default_code']['invisible'] = True
        return result """