from odoo import fields, models, api


class ServiceCategories(models.Model):
    _name = "service.category"
    _description = "Service Categories"

    service_categ_id = fields.Many2one("service.category", "Types")
    product_categ_id = fields.Many2one('product.category', " Category", delegate=True, copy=False,
                                       ondelete="cascade", )

    def write(self, vals):
        if "service_categ_id" in vals:
            categ = self.env["service.category"].browse(vals['service.category'])
            vals.update({"categ_id": categ.product_categ_id.id})
        return super(ServiceCategories, self).write(vals)
    #
    def unlink(self):
        rec = self.env["product.category"].sudo().browse(self.product_categ_id.id)
        rec.unlink()
        return super(ServiceCategories, self).unlink()
    #
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        """For adding '(copy)' string into name while duplicating a record"""

        self.ensure_one()
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)", self.name)
        return super(ServiceCategories, self).copy(default=default)

