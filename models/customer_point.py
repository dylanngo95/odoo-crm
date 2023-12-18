# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Customer_Point(models.Model):
    _name = "courts.customer_point"
    _description = "This module include customer service and loyalty service"
    user_id = fields.Integer(string = 'Customer Id', required = True)
    order_id = fields.Integer(string = 'Order Id', required = True)
    point = fields.Float(string = 'Customer Earn Point', required = True)
    amount_spent = fields.Float(string = 'Amount Spent', required = True)
