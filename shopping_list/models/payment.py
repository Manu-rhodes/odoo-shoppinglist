from odoo import fields, models


class payment(models.Model):
    _name = 'sl.payment'
    _description = 'Payment'

    supplier = fields.Char(string='Name of Supplier')
    total = fields.Float(string='Grand Total')
    date = fields.Date(string='Payment Date')
          