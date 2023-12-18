# -*- coding: utf-8 -*-

from odoo import api, fields, models

class customer_point(models.Model):
    _name = 'courts_crm.customer_point'
    _description = 'courts_crm.customer_point'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100