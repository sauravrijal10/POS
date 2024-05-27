from odoo import models, fields

class MyPosConfig(models.Model):
    _name= 'pos.config'
    _inherit = 'pos.config'


    shop_name=fields.Char(string="Shop") 