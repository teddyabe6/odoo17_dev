# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Farmer(models.Model):
    """ This model represents farmer."""
    _name = 'farmer.management'
    _description = 'Farmer Management'

    name = fields.Char(string="Farmer Name", required=True)
    phone = fields.Char(string="Phone Number")
    age = fields.Integer(string="Age")
    village = fields.Char(string="Village")

    land_ids = fields.One2many(
        'farmer.land',
        'farmer_id',
        string="Lands"
    )

    total_land_area = fields.Float(
        string="Total Land (Hectares)",
        compute="_compute_total_land_area",
        store=True
    )

    @api.depends('land_ids.size_in_hectares')
    def _compute_total_land_area(self):
        for farmer in self:
            farmer.total_land_area = sum(farmer.land_ids.mapped('size_in_hectares'))