from odoo import fields, models, api


class HotelService(models.Model):
    _name = "hotel.service"
    _description = "Hotel Service"

    product_id = fields.Many2one('product.product', "Services", required=True, delegate=True, ondelete="cascade", )
    category_id = fields.Many2one("service.category", "Category", required=True, ondelete="restrict", )
    manager_id = fields.Many2one("res.users", string='Manager')

    # @api.model
    # def create(self, vals):
    #     if "category_id" in vals:
    #         prod = self.env["service.category"].browse(vals["category_id"])
    #         vals.update({"categ_id": prod.product_categ_id.id, 'service_ok': True})
    #     return super(HotelService, self).create(vals)
    #
    # def write(self, vals):
    #     if "category_id" in vals:
    #         prod = self.env["service.category"].browse(vals["category_id"])
    #         vals.update({"categ_id": prod.product_categ_id.id,'service_ok': True})
    #     return super(HotelService, self).write(vals)
    #
    # def unlink(self):
    #     rec = self.env["product.product"].sudo().browse(self.product_id.id)
    #     rec.unlink()
    #     return super(HotelService, self).unlink()
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
    #     return super(HotelService, self).copy(default=default)