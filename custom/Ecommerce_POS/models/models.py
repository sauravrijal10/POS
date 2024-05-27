# pos_config.py
from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    printer_ids = fields.Many2many(
        comodel_name='pos.printer',
        relation='pos_config_printer_rel',  # Ensure unique relation table
        column1='config_id',
        column2='printer_id',
        string='Config Printers'
    )
class PosFront(models.Model):
    _name = 'pos.front'
    _description = 'POS Front'
    _inherit = 'pos.config'

    name = fields.Char("Name")
    
    printer_ids = fields.Many2many(
        comodel_name='pos.printer',
        relation='pos_front_printer_rel',  # Ensure this is different from pos_config_printer_rel
        column1='front_id',  # Use a different column name if necessary
        column2='printer_id',
        string='Front Printers'
    )