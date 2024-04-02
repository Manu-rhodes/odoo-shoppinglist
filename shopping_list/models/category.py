from odoo import fields, models


class category(models.Model):
    _name = 'sl.category'
    _description = 'Product Categories'

    name = fields.Char(string='Name of Category', required=True)
    description = fields.Text(string='Description')
    product_ids = fields.One2many('sl.product', 'category_id', string='Products', readonly=True)
    