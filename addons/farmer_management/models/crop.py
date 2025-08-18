# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Crop(models.Model):
    """ This model represents crop."""
    _name = 'farmer.crop'
    _description = 'Crop Information'

    name = fields.Char(string="Crop Name", required=True)
    season = fields.Selection(
        [('summer', 'Summer'), ('winter', 'Winter')],
        string="Season"
    )
    expected_yield = fields.Float(string="Expected Yield (Quintal)")

    land_id = fields.Many2one(
        'farmer.land',
        string="Land",
        ondelete='cascade'
    )