from odoo import models, fields

class SalesDetails(models.Model):
    _name = 'sales.details'
    _inherit = 'pos.details.wizard'

#     # Define a Many2one field referencing the pos.details.wizard model
#     # pos_details_id = fields.Many2one('pos.details.wizard', string="POS Details")
    name = fields.Char(string="Name")
