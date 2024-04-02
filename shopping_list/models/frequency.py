from odoo import fields, models


class frequency(models.Model):
    _name = 'sl.frequency'
    _description = 'Frequency'

    duration = fields.Integer(string='Frequency Duration')
    unit = fields.Selection([
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year')
    ], string='Unit')
    last_date_added = fields.Char(string='Last Date Added')
    product_ids = fields.One2many('sl.product', 'frequency_id', string='Products', readonly=True)
