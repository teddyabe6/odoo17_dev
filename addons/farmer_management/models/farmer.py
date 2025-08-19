from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Farmer(models.Model):
    _name = 'farmer.management'
    _description = 'Farmer'
    _order = 'name'

    name = fields.Char(string="Farmer Name", required=True)
    phone = fields.Char(string="Phone")
    age = fields.Integer(string="Age")
    village = fields.Char(string="Village")

    land_ids = fields.One2many('farmer.land', 'farmer_id', string="Lands")
    family_ids = fields.One2many('farmer.family', 'farmer_id', string="Family Members")

    total_land_area = fields.Float(
        string="Total Land (Hectares)",
        compute="_compute_total_land_area",
        store=True
    )

    @api.depends('land_ids.size_in_hectares')
    def _compute_total_land_area(self):
        for farmer in self:
            farmer.total_land_area = sum(farmer.land_ids.mapped('size_in_hectares'))

    _sql_constraints = [
        ('phone_unique', 'unique(phone)', 'Phone number must be unique among farmers.')
    ]

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age is not None and rec.age < 0:
                raise ValidationError("Age cannot be negative.")
