# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class CustomerPoint(models.Model):
    _name = 'courts_crm.customer_points'
    _description = 'courts_crm.customer_points'

    code = fields.Char()
    user_id = fields.Integer()
    points = fields.Float()
    expiration_date = fields.Date()

    order_id = fields.Many2one(
        comodel_name='sale.order',
        string="Order Reference",
        required=True, ondelete='cascade', index=True, copy=False)
    sequence = fields.Integer(string="Sequence", default=10)

    @api.constrains('code')
    def _check_code_unique(self):
        code_counts = self.search_count([('code', '=', self.code), ('id', '!=', self.id)])
        if code_counts > 0:
            raise ValidationError("The code is unique.")

    @api.depends('points', 'user_id')
    def _compute_points(self):
        for record in self:
            tmp = record
            print("1")
            print(tmp)

    @api.onchange('user_id')
    def _onchange_user_id(self):
        for record in self:
            tmp = record
            print("2")
            print(tmp)
