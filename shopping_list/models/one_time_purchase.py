from odoo import fields, models


class one_time_purchase(models.Model):
    _name = 'sl.one.time.purchase'
    _description = 'One Time Purchase'

    product_id = fields.Integer(string='Product ID')
    name = fields.Char(string='Product Name')
    quantity = fields.Integer(string='Quantity')
    approval_status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Approval Status')
    approval_date = fields.Date(string='Date of Approval')
    added = fields.Boolean(string='Added')
    