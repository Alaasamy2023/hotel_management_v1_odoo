from odoo import fields, models, api


class AmenityTypes(models.Model):
    _name = "amenity.types"
    _description = "Amenity Types"

    amenity_type_id = fields.Many2one("amenity.types", "Types")
    categ_id = fields.Many2one('product.category', "Product Category", delegate=True, copy=False, ondelete="cascade")

    # def write(self, vals):
    #     if "amenity_type_id" in vals:
    #         amenity_categ = self.env["amenity.type"].browse(vals['amenity_type_id'])
    #         vals.update({"categ_id": amenity_categ.categ_id.id})
    #     return super(AmenityTypes, self).write(vals)
    #
    # def unlink(self):
    #     rec = self.env["product.category"].sudo().browse(self.categ_id.id)
    #     rec.unlink()
    #     return super(AmenityTypes, self).unlink()
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
    #     return super(AmenityTypes, self).copy(default=default)
