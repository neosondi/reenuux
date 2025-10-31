from odoo import models, fields

class Progression(models.Model):
    _name = 'scout.progression'
    _description = 'Scout Progression Step'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    badge_id = fields.Many2one('scout.badge', string='Badge')
