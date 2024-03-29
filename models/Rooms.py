from odoo import fields, models, api, _


class Rooms(models.Model):
    _name = "room.room"
    _description = 'Rooms'

    floor_id = fields.Many2one('hotel.floor', string='Floor')
    type_id = fields.Many2one('room.types', string='Type',required=True)
    product_id = fields.Many2one('product.product', "product_id", required=True, delegate=True, ondelete="cascade")
    amenity_ids = fields.Many2many('hotel.amenity')
    status = fields.Selection([("available", "Available"), ("occupied", "Occupied"), ('book', 'Booked')],
                              default="available")
    manager_id = fields.Many2one('res.users', string='Manager')

    # @api.model
    # def create(self, vals):
    #     if "type_id" in vals:
    #         prod = self.env["room.types"].browse(vals["type_id"])
    #         vals.update({"categ_id": prod.categ_id.id, 'room_ok': True})
    #     return super(Rooms, self).create(vals)
    #
    # def write(self, vals):
    #     if "type_id" in vals:
    #         prod = self.env["room.types"].browse(vals["type_id"])
    #         vals.update({"categ_id": prod.categ_id.id})
    #     return super(Rooms, self).write(vals)
    #
    # def unlink(self):
    #     rec = self.env["product.product"].sudo().browse(self.product_id.id)
    #     rec.unlink()
    #     return super(Rooms, self).unlink()
    #
    # @api.returns('self', lambda value: value.id)
    # def copy(self, default=None):
    #     """For adding '(copy)' string into name while duplicating a record"""
    #
    #     self.ensure_one()
    #     if default is None:
    #         default = {}
    #     if 'name' not in default:
    #         default['name'] = _("%s (copy)", self.name)
    #     return super(Rooms, self).copy(default=default)


class RoomTypes(models.Model):
    _name = "room.types"
    _description = 'Room Types'

    room_type_id = fields.Many2one("room.types", "Types")
    categ_id = fields.Many2one('product.category', "Product Category", delegate=True, copy=False, ondelete="cascade")
    num_person = fields.Integer(string='Number of persons',required=True)

    # @api.model
    # def create(self, vals):
    #     vals.update({'is_room_categ': True})
    #     return super(RoomTypes, self).create(vals)
    #
    # def write(self, vals):
    #     if "room_type_id" in vals:
    #         categ = self.env["room.types"].browse(vals['room_type_id'])
    #         vals.update({"categ_id": categ.categ_id.id})
    #     return super(RoomTypes, self).write(vals)
    #
    # def unlink(self):
    #     rec = self.env["product.category"].sudo().browse(self.categ_id.id)
    #     rec.unlink()
    #     return super(RoomTypes, self).unlink()
    #
    # @api.returns('self', lambda value: value.id)
    # def copy(self, default=None):
    #     """For adding '(copy)' string into name while duplicating a record"""
    #
    #     self.ensure_one()
    #     if default is None:
    #         default = {}
    #     if 'name' not in default:
    #         default['name'] = _("%s (copy)", self.name)
    #     return super(RoomTypes, self).copy(default=default)

