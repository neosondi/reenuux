from odoo import models, fields

class Badge(models.Model):
    _name = 'scout.badge'
    _description = 'Scout Badge'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')
