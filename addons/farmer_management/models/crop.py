from odoo import models, fields

class Crop(models.Model):
    _name = 'farmer.crop'
    _description = 'Crop'
    _order = 'name'

    name = fields.Char(string="Crop Name", required=True)
    season = fields.Selection(
        [('summer', 'Summer'), ('winter', 'Winter'), ('spring', 'Spring'), ('autumn', 'Autumn')],
        string="Season",
        default='summer'
    )
    expected_yield = fields.Float(string="Expected Yield (Quintal)")

    land_id = fields.Many2one('farmer.land', string="Land", ondelete='cascade')

    # Related helper to see farmer on crop (handy for search/grouping)
    farmer_id = fields.Many2one(
        'farmer.management',
        string="Farmer",
        related='land_id.farmer_id',
        store=True,
        readonly=True
    )
