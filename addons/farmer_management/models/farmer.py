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