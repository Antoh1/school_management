# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'school.course'
    _description = 'School Course Management'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Course Description")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
