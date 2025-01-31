# -*- coding: utf-8 -*-
# from odoo import http


# class MbsInstituto(http.Controller):
#     @http.route('/mbs_instituto/mbs_instituto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mbs_instituto/mbs_instituto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mbs_instituto.listing', {
#             'root': '/mbs_instituto/mbs_instituto',
#             'objects': http.request.env['mbs_instituto.mbs_instituto'].search([]),
#         })

#     @http.route('/mbs_instituto/mbs_instituto/objects/<model("mbs_instituto.mbs_instituto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mbs_instituto.object', {
#             'object': obj
#         })

