from odoo import models, fields

class FamilyMember(models.Model):
    _name = 'farmer.family'
    _description = 'Family Member'
    _order = 'member_name'

    farmer_id = fields.Many2one('farmer.management', string="Farmer", ondelete='cascade')
    member_name = fields.Char(string="Name", required=True)
    relation = fields.Selection(
        [('spouse', 'Spouse'), ('child', 'Child'), ('parent', 'Parent'), ('other', 'Other')],
        string="Relation",
        required=True
    )
    age = fields.Integer(string="Age")
