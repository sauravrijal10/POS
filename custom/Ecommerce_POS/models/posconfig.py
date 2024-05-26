from odoo import models, fields, api

class CustomPOSConfig(models.Model):
    _name = 'custompos.config'
    _inherit = 'pos.config'

    custom_field = fields.Char(string='Custom Field')

    # @api.model
    # def create(self, values):
    #     # Custom logic before creating a POS order
    #     return super(CustomPOSOrder, self).create(values)

    # def custom_method(self):
    #     # Your custom method
    #     pass
