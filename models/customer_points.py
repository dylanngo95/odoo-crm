# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomerPoint(models.Model):
    _name = 'courts_crm.customer_points'
    _description = 'courts_crm.customer_points'

    code = fields.Char()
    user_id = fields.Integer()
    points = fields.Float()
    expiration_date = fields.Date()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
