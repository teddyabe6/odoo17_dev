# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Land(models.Model):
    """ This model represents land."""
    _name = 'farmer.land'
    _description = 'Farmer Land'

    name = fields.Char(string="Land Name", required=True)
    size_in_hectares = fields.Float(string="Size (Hectares)")
    location = fields.Char(string="Location")

    farmer_id = fields.Many2one(
        'farmer.management',
        string="Farmer",
        ondelete='cascade'
    )
