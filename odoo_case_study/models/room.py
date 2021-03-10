# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class TypewiserRoom(models.Model):
    _name = 'typewiser.room'
    _description = 'Room'

    name = fields.Char(string="Name")
    capacity = fields.Integer("Capacity")
    attendees_limit = fields.Integer("No of Attendees")
    status = fields.Selection([('yes', 'Available'), ('no', 'Booked')], default='yes')

    @api.constrains('attendees_limit')
    def _check_attendees_limit(self):
        for room in self:
            if room.attendees_limit > room.capacity:
                raise Warning(_("No of Attendees must be equal or less to Room Capacity!!"))
