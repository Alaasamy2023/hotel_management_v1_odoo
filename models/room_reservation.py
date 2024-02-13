# -*- coding: utf-8 -*-

from odoo import fields, models, api, _, exceptions
from datetime import datetime
from odoo.exceptions import ValidationError


class RoomOrder(models.Model):
    _inherit = 'sale.order'
    # _name = "hotel.RoomOrder"
    _description = "Hotel RoomOrder"

    num_person = fields.Integer(string='Number of Persons', default=1,required=True)













