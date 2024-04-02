from odoo import fields, models


class list(models.Model):
    _name = 'sl.list'
    _description = "Shopping List"

    date = fields.Date(string='Date')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string='Status', default='draft')
    line_ids = fields.One2many('sl.list.line', 'list_id', string='Products')
    one_time = fields.Boolean(string='One Time')
