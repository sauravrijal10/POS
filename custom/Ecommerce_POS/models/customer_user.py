from odoo import models, fields, api, _

class User(models.Model):
    _name = 'custom.user'
    _inherit = 'res.partner'

    username = fields.Char(string='Username', required=True, tracking=True)
    password = fields.Char(string='Password', required=True)