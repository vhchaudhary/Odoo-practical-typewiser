# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPatner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Char(string="Instructor")
    courses_ids = fields.Many2many('typewiser.course', 'partner_course_rel', 'partner_id', 'course_id',
                                   string="Courses")
