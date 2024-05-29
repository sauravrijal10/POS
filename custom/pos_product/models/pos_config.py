from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    iface_product_label = fields.Boolean(
        string="Print Product Labels",
        help="Display a button to print Product Labels for ordered products",
        default=True,
    )