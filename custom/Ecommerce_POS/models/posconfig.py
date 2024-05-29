from odoo import models, fields, api

""" class CustomPOSConfig(models.Model):
    _name = 'custompos.config'
    _inherit = 'pos.config'

    _description = 'POS Front'
    _inherit = 'pos.config'

    name = fields.Char("Name")
    
    printer_ids = fields.Many2many(
        comodel_name='pos.printer',
        relation='pos_front_printer_rel',  
        column1='front_id',  
        column2='printer_id',
        string='Front Printers'
    )

class PosConfig(models.Model):
    _inherit = 'pos.config'

    printer_ids = fields.Many2many(
        comodel_name='pos.printer',
        relation='pos_config_printer_rel',  
        column1='config_id',
        column2='printer_id',
        string='Config Printers'
    ) """


class PosConfig(models.Model):
    _inherit = 'pos.config'

    custom_field = fields.Char(string='Custom Field') 

   
    def action_open_session(self):
        # Your implementation for opening a session
        pass

   
    def action_close_session(self):
        # Your implementation for closing a session
        pass

    


    