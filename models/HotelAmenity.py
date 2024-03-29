from odoo import fields, models, api




class HotelAmenity(models.Model):
    _name = "hotel.amenity"
    _description = "Hotel Amenities"

    product_id = fields.Many2one('product.product', "Amenities", required=True, delegate=True, ondelete="cascade", )
    type_id = fields.Many2one("amenity.types", "Amenity Type", required=True, ondelete="restrict", )
    manager_id = fields.Many2one("res.users", string='Manager')

    @api.model
    def create(self, vals):
        if "type_id" in vals:
            prod = self.env["amenity.types"].browse(vals["type_id"])
            vals.update({"categ_id": prod.categ_id.id})
        return super(HotelAmenity, self).create(vals)

    def write(self, vals):
        if "type_id" in vals:
            prod = self.env["amenity.types"].browse(vals["type_id"])
            vals.update({"categ_id": prod.categ_id.id})
        return super(HotelAmenity, self).write(vals)

    def unlink(self):
        rec = self.env["product.product"].sudo().browse(self.product_id.id)
        rec.unlink()
        return super(HotelAmenity, self).unlink()

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        """For adding '(copy)' string into name while duplicating a record"""

        self.ensure_one()
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)", self.name)
        return super(HotelAmenity, self).copy(default=default)