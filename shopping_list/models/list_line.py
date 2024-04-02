from odoo import fields, models


class list_line(models.Model):
    _name = 'sl.list.line'
    _description = "Shopping List Line"

    list_id = fields.Many2one('sl.list', string='Shopping List')
    product_id = fields.Many2one('sl.product', string='Product')
    quantity = fields.Integer(string='Quantity')
    remove = fields.Boolean(string='Remove')
