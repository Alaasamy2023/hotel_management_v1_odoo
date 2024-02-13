# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class HotelMeals(models.Model):
    _name = 'hotel.meals'
    _description = 'Meals'

    meal_type_id = fields.Many2one('meal.types', string='Type', required=True, ondelete="cascade")
    product_id = fields.Many2one('product.product', "Meal", required=True, delegate=True, ondelete="cascade")
    manager_id = fields.Many2one("res.users", string='Manager')


    # @api.model
    # def create(self, vals):
    #     if "meal_type_id" in vals:
    #         prod = self.env["meal.types"].browse(vals["meal_type_id"])
    #         vals.update({"categ_id": prod.product_categ_id.id, 'meals_ok': True})
    #     return super(HotelMeals, self).create(vals)
    #
    # def write(self, vals):
    #     if "meal_type_id" in vals:
    #         prod = self.env["meal.types"].browse(vals["meal_type_id"])
    #         vals.update({"categ_id": prod.product_categ_id.id})
    #     return super(HotelMeals, self).write(vals)
    #
    # def unlink(self):
    #     rec = self.env["product.product"].sudo().browse(self.product_id.id)
    #     rec.unlink()
    #     return super(HotelMeals, self).unlink()
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
    #     return super(HotelMeals, self).copy(default=default)




























































class MealsTypes(models.Model):
    _name = "meal.types"
    _description = "Meals Types"

    type_id = fields.Many2one("meal.types", "Types")
    product_categ_id = fields.Many2one('product.category', "Product Category", delegate=True, copy=False,
                                       ondelete="cascade")

    # @api.model
    # def create(self, vals):
    #     vals.update({'is_meals_categ': True})
    #     return super(MealsTypes, self).create(vals)
    #
    # def write(self, vals):
    #     if "type_id" in vals:
    #         categ = self.env["meal.type"].browse(vals['meal'])
    #         vals.update({"categ_id": categ.product_categ_id.id})
    #     return super(MealsTypes, self).write(vals)
    #
    # def unlink(self):
    #     rec = self.env["product.category"].sudo().browse(self.product_categ_id.id)
    #     rec.unlink()
    #     return super(MealsTypes, self).unlink()
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
    #     return super(MealsTypes, self).copy(default=default)


