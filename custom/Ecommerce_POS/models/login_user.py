from odoo import models, fields, api

class LoginUser(models.Model):
    _inherit = 'res.users'

    isAdmin = fields.BooleanField(_("is admin"),)