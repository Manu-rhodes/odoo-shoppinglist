from odoo import api, fields, models, _


class budget(models.Model):
    _name = 'sl.budget'
    _description = 'Budget'

    actual = fields.Float(string='Actual Budget')
    expected = fields.Float(string='Expected Budget')
    ref = fields.Char(string="Reference", default=lambda self:_('New'))


    @api.model_create_multi
    def create(self, val_list):
        for vals in val_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('sl.budget')
        return super(budget, self).create(val_list)  
