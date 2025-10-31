from odoo import models, fields

class Scout(models.Model):
    _name = 'scout.scout'
    _description = 'Scout'

    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    unit_id = fields.Many2one('scout.unit', string='Unit')
    progression_step_ids = fields.Many2many('scout.progression', string='Progression Steps')
    badge_ids = fields.Many2many('scout.badge', string='Badges')
