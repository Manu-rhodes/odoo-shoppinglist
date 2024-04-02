from odoo import fields, models


class product(models.Model):
    _name = 'sl.product'
    _description = 'Product'

    name = fields.Char(string='Product Name', required=True)
    description = fields.Text(string='Product Description')
    qty_available = fields.Integer(string='Quantity Available')
    price = fields.Float(string='Price')
    category_id = fields.Many2one('sl.category', string='Category', required=True)
    flag = fields.Boolean(string='Flag')
    frequency_id = fields.Many2one('sl.frequency', string='Frequency')
