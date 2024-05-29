from odoo import models, fields, api

class CustomPosConfig(models.Model):
    _name = 'custom.pos.config'
    _inherits = {'pos.config': 'pos_config_id'}

    pos_config_id = fields.Many2one('pos.config', required=True, ondelete='cascade', string='Point of Sale')
    custom_field = fields.Char(string="Custom Field")

class PosConfig(models.Model):
    _inherit = 'pos.config'

    custom_pos_config_id = fields.One2many('custom.pos.config', 'pos_config_id', string='Custom POS Config')
    custom_field = fields.Char(string="Custom Field", compute='_compute_custom_field')

    @api.depends('custom_pos_config_id.custom_field')
    def _compute_custom_field(self):
        for record in self:
            custom_fields = record.custom_pos_config_id.mapped('custom_field')
            record.custom_field = custom_fields[0] if custom_fields else False
