# -*- coding: utf-8 -*-
# from odoo import http


# class LogisticaMca(http.Controller):
#     @http.route('/logistica_mca/logistica_mca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/logistica_mca/logistica_mca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('logistica_mca.listing', {
#             'root': '/logistica_mca/logistica_mca',
#             'objects': http.request.env['logistica_mca.logistica_mca'].search([]),
#         })

#     @http.route('/logistica_mca/logistica_mca/objects/<model("logistica_mca.logistica_mca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('logistica_mca.object', {
#             'object': obj
#         })
