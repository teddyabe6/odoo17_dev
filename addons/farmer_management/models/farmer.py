from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Farmer(models.Model):
    _name = 'farmer.management'
    _description = 'Farmer'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = 'name'

    name = fields.Char(string="Farmer Name", required=True)
    phone = fields.Char(string="Phone")
    age = fields.Integer(string="Age")
    village = fields.Char(string="Village")
    partner_id = fields.Many2one("res.partner", string="Partner", required=True, tracking=True)
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

    @api.model
    def create(self, vals):
        record = super().create(vals)

        # Send chatter message
        record.message_post(
            body=_("Change request created for partner: %s") % record.partner_id.name,
            subtype_xmlid="mail.mt_comment"
        )

        # Assign activity to a group (example: system user group)
        group = self.env.ref("base.group_system")  # change to your target group
        users = group.users
        for user in users:
            record.activity_schedule(
                "mail.mail_activity_data_todo",
                user_id=user.id,
                summary=_("Review Partner Change Request"),
                note=_("User %s requested a change on %s") % (self.env.user.name, record.partner_id.name),
            )

        return record
