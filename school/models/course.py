from odoo import api, fields, models, _

class Course(models.Model):
    _name = 'school.course'
    _description = 'course'
    name = fields.Char('Course Name', reqired=True)
    code = fields.Char('Code')