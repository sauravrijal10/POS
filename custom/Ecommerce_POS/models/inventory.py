from odoo import models, fields

class InventoryModel(models.Model):
    _name = 'custom.stock'
    _inherit='stock.picking'

    pos_session_id = fields.Many2one('pos.session', index=True)
    pos_order_id = fields.Many2one('pos.order', index=True)

    # Add your custom fields or override existing ones if needed
