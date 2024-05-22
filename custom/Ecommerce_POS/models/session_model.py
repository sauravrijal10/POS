from odoo import fields, models,api

class CustomSession(models.Model):
    _name ='custom.session'
    _inherit = 'pos.session'
    

    session_name = fields.Char(string='Session Name')
    order_ids = fields.One2many('pos.order', 'session_id', string='Orders')
    pos_config_id = fields.Many2one('pos.config', string='Point of Sale', required=True)

    @api.model
    def create(self, vals):
        if 'pos_config_id' not in vals:
            raise ValueError("You should assign a Point of Sale to your session.")
        return super(CustomSession, self).create(vals)

    @api.model
    def create_order(self, order_vals):
        """
        Create a new order within the session.
        :param order_vals: Dictionary containing order values
        :return: Created order record
        """
        session_id = order_vals.get('session_id')
        if session_id:
            session = self.browse(session_id)
            if session:
                order_vals['session_id'] = session_id
                order = self.env['pos.order'].create(order_vals)
                return order
            else:
                raise ValueError("Session not found.")
        else:
            raise ValueError("Session ID not provided.")