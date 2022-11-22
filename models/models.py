# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Course(models.Model):
    _name = 'school.course'
    _description = 'School Course Management'

    name = fields.Char(string="Title", required=True)
    responsible_user = fields.Many2one('res.users', string="Responsible")
    session_list = fields.One2many("course.session", 'course_id', string="Session List")
    tutor = fields.Many2one('res.partner', string="Instructor")
    #tutor = fields.Char(related="session_id.tutor")
    session_id = fields.Many2one("course.session", string="Session")
    description = fields.Text(string="Course Description")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



class Session(models.Model):
    _name = 'course.session'
    _description = 'Sessions for the courses offered'

    name = fields.Char(string="Session")
    course_id = fields.Many2one('school.course', 'Course')
    tutor = fields.Many2one('res.partner', string="Instructor")
    session_start = fields.Datetime(string="Session Starts")
    session_end = fields.Datetime(string="Session Ends")
    duration = fields.Float(string="Session Duration(HRs)")
    seats = fields.Integer(string="No Of Seats")
    description = fields.Char(string="Session Details")
    attendee_list = fields.Many2many("res.partner", "session_attendee_rel", "session_id", "attendee_id", string="Students")
    
    # @api.depends('start_time','end_time')
    # def _compute_duration(self):
    #     for record in self:
    #         difference = self.end_time - self.start_time
    #         difference_in_sec = difference.total_seconds()
    #         record['duration'] = difference_in_sec/3600.0

    #inputing start date and duration, calculates the end time for the session
    @api.onchange('session_start')
    def onchange_session_start(self):
        if self.session_start:
            session_start = fields.Datetime.from_string(self.session_start)
            interval = datetime.timedelta(seconds=(self.duration * 3600))
            self.session_end = fields.Datetime.to_string(session_start + interval)


class Attendees(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(string="Student")
