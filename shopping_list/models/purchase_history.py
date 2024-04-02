from odoo import api,fields, models



class purchase(models.Model):
    _name = 'sl.purchase.history'
    _description = "Purchase History"

    user_ids = fields.Integer(string='User ID')
    list_ids = fields.Many2one('sl.list', string='List')
    product_ids = fields.Many2one('sl.product', string='Product')
    product_name = fields.Char(string='Product Name')
    unit_price = fields.Float(string='Unit Price')
    quantity = fields.Integer(string='Quantity')
    sub_total = fields.Float(string='Sub Total')
    location = fields.Char(string='Purchase Location')
    promotion_on_product = fields.Boolean(string='Promotion')
    discount = fields.Float(string='Discount')
    date = fields.Date(string='Date of Purchase')

    @api.onchange('discount')
    def onchange_discount(self):
        if self.discount >= 0:
            self.promotion_on_product = True
        else:
            self.promotion_on_product = False

   
    