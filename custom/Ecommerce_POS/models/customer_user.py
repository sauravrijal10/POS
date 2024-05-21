from odoo import models, fields, api, _

class User(models.Model):
    _name = 'custom.user'
    # _inherit = 'res.partner'
    _inherits = {'res.partner': 'partner_id'}


    username = fields.Char(string='Username', required=True, tracking=True)
    password = fields.Char(string='Password', required=True)
    partner_id = fields.Many2one('res.partner', required=True, ondelete="cascade", string="Related Partner")

    channel_ids = fields.Many2many('mail.channel', 'mail_channel_profile_partner', 'partner_id', 'channel_id')

