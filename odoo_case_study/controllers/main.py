# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.http import request, route
from odoo import http

from odoo.addons.portal.controllers.portal import get_records_pager, CustomerPortal


class Academy(CustomerPortal):

    def _prepare_portal_layout_values(self):
        values = super(Academy, self)._prepare_portal_layout_values()
        Ticket = request.env['typewiser.course']
        tickets_count = Ticket.search_count([])
        values['tickets_count'] = tickets_count
        return values

    @http.route(['/course'], type='http', auth="public", website=True)
    def portal_my_tickets(self, **kw):
        values = self._prepare_portal_layout_values()
        course_id = request.env['typewiser.course'].search([])
        values.update({
            'page_name': 'Tickets',
            'courses': course_id,
        })
        return request.render("odoo_case_study.portal_my_tickets", values)
