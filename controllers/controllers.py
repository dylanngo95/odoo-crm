# -*- coding: utf-8 -*-
# from odoo import http


# class CourtsCrm(http.Controller):
#     @http.route('/courts_crm/courts_crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/courts_crm/courts_crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('courts_crm.listing', {
#             'root': '/courts_crm/courts_crm',
#             'objects': http.request.env['courts_crm.courts_crm'].search([]),
#         })

#     @http.route('/courts_crm/courts_crm/objects/<model("courts_crm.courts_crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('courts_crm.object', {
#             'object': obj
#         })

