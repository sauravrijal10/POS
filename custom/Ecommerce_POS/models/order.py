from odoo import models, fields

class CustomOrder(models.Model):
    _name = "custom.order"
    _inherit = "pos.order"
