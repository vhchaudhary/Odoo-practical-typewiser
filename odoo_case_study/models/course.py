# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class TypewiserCourse(models.Model):
    _name = 'typewiser.course'
    _description = 'Course'

    name = fields.Char(string="Name")
    partner_id = fields.Many2one('res.partner', string="Instructor")
    room_id = fields.Many2one('typewiser.room')
    attendee_ids = fields.Many2many('res.partner', 'course_partner_rel', 'course_id', 'partner_id',
                                    string="Attendees")
    lesson_ids = fields.Many2many('typewiser.lesson', string="Lessons")
    description = fields.Text(string="Description")

    @api.onchange('partner_id', 'attendee_ids')
    def _onchange_partner_id(self):
        if self.partner_id:
            partner_ids = self.env['res.partner'].search([('id', '!=', self.partner_id.id or False)])
            return {'domain': {'attendee_ids': [('id', 'in', partner_ids.ids)]}}

    @api.constrains('attendee_ids')
    def _check_attendee_ids(self):
        for course in self:
            if course.attendee_ids and course.partner_id and course.partner_id.id in course.attendee_ids.ids:
                raise Warning(_("Same person can not apply for attendee and Instructor both!!"))


class TypewiserLesson(models.Model):
    _name = 'typewiser.lesson'
    _description = 'Lesson'

    name = fields.Char(string="Name")
    room_id = fields.Many2one('typewiser.room', string="Room")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")

    @api.constrains('start_time', 'end_time')
    def _check_lesson_time(self):
        for lesson in self:
            if lesson.start_time > lesson.end_time:
                raise Warning(_("End time must be greter to start time!!"))

    @api.onchange('room_id', 'start_time', 'end_time')
    def _onchange_room_available(self):
        if self.room_id and self.start_time and self.end_time:
            flag = self.env['typewiser.lesson'].search([('start_time', '>=', self.start_time),
                                                        ('start_time', '<=', self.end_time),
                                                        ('room_id', '=', self.room_id.id)])
            if flag:
                raise Warning(_("This Room not available between this time!!"))
