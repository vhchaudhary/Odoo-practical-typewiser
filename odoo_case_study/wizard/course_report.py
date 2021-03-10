# -*- coding: utf-8 -*-

from odoo import models, fields


class WizCourseReport(models.TransientModel):
    _name = 'wiz.course.report'
    _desription = "Course Report"

    course_ids = fields.Many2many('typewiser.course', 'course_report_course_rel',
                                  'report_id', 'course_id', string="Courses")

    def print_course_report(self):
        course_list = []
        if self.course_ids:
            course_ids = self.course_ids
        else:
            course_ids = self.env['typewiser.course'].search([])
        if course_ids:
            for rec in course_ids:
                course_list.append({
                    'name': rec.name,
                    'room_id': rec.room_id.name,
                    'partner_id': rec.partner_id.name,
                    'lesson_ids': [[ls.name, ls.start_time, ls.end_time] for ls in rec.lesson_ids]
                })
        datas = {
            'model': 'typewiser.course',
            'course_ids': course_list
        }
        return self.env.ref('odoo_case_study.course_report_tw').report_action(self, data=datas)

