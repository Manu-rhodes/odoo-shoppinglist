from odoo import fields, models


class notification(models.Model):
    _name = 'sl.notification'
    _description = 'Notification'

    message = fields.Text(string='Message')
    timestamp = fields.Date(string='Time Stamp')
    read_status = fields.Boolean(string='Read Status')
    user_id = fields.Many2one('sl.user', string='User')
