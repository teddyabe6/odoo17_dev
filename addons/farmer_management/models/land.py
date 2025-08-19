from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Land(models.Model):
    _name = 'farmer.land'
    _description = 'Land'
    _order = 'name'

    name = fields.Char(string="Land Name", required=True)
    size_in_hectares = fields.Float(string="Size (Hectares)")
    location = fields.Char(string="Location")

    farmer_id = fields.Many2one('farmer.management', string="Farmer", ondelete='cascade')

    crop_ids = fields.One2many('farmer.crop', 'land_id', string="Crops")

    @api.constrains('size_in_hectares')
    def _check_size(self):
        for rec in self:
            if rec.size_in_hectares is not None and rec.size_in_hectares < 0.1:
                raise ValidationError("Land size must be at least 0.1 hectare.")
