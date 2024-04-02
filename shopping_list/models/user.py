from odoo import fields, models


class user(models.Model):
    _name = "sl.user"
    _description = 'Shopping List User'

    first_name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    email = fields.Char("Email Address")
    password = fields.Char("Password")
