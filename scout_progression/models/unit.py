from odoo import models, fields

class Unit(models.Model):
    _name = 'scout.unit'
    _description = 'Scout Unit'

    name = fields.Char(string='Name', required=True)
    leader_id = fields.Many2one('res.partner', string='Leader')
