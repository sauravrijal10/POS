from odoo import models,fields

class Report(models.Model):
    _name = 'pos.report'
    _inherit = 'report.pos.order'

    name = fields.Char(string="Name")


    