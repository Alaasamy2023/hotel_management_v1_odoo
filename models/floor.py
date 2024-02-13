from odoo import models, fields, api


class Floor(models.Model):
    _name = "hotel.floor"
    _description = "Floor"

    name = fields.Char(string="Name", required=True)

