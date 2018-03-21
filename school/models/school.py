from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as df

class School(models.Model):
    _name = 'school.school'

    name = fields.Char('Name', required=True)
    add = fields.Char('Address')
    total_stud = fields.Char('Total Student')
    student_ids = fields.One2many('school.student', 'school_id', 'Students')

    @api.multi
    def call_method(self):
        print "--call_method-->", type(self)
        self.total_stud = len(self.env['school.student'].search([('school_id', '=', self.id)]))

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        res = super(School, self).search_read(domain, fields, offset, limit, order)
        print "--search_read-->", type(res)
        # print '========>', res
        return res

    @api.model
    def create(self, vals):
        print "-----------vals----------", vals
        print "-----------type----------", type(vals)
        res = super(School, self).create(vals)
        print '------------res----------', res
        print '-----------type_create----------', type(res)

        if res.name:
            self.env['school.student'].create({
                'name': res.name,
                'school_id': res.id
            })
        return res

    @api.multi
    def write(self, vals):
        # print "---------->", vals
        res = super(School, self).write(vals)
        print '----type_write--------->', type(res)
        return res

    @api.multi
    def unlink(self):
        # print '--------------->', self
        res = super(School, self).unlink()
        print '---type_unlink------>', type(res)
        return res

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        # print '---self--->', self, fields, load
        res = super(School, self).read(fields, load)
        print '----type_read-->', type(res)
        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):

        args = args or []
        # print '--aa--->', args
        data = []
        # print '---dd--->', data
        if name:
            data = ['|', ('name', operator, name), ('add', operator, name)]
        res = self.search(data + args, limit=limit)
        print '===type_name_search==>>>>', type(res)
        return res.name_get()

    @api.multi
    def name_get(self):
        r = []
        for res in self:
            name = res.name
            if res.add:
                name = name + ' ' + '(' + res.add + ')'
            r.append((res.id, name))
            print "--type_name_get-->", type(r)
        return r


class Student(models.Model):
    _name = 'school.student'

    name = fields.Char('Name', required=True)
    add = fields.Char('Address')
    age = fields.Integer('Age')
    email = fields.Char('Email')
    birth_date = fields.Date('Birth Date')
    school_id = fields.Many2one('school.school', 'School')

    @api.constrains('age', 'birth_date')
    def check(self):

        dt = datetime.strptime(self.birth_date, df)
        bdt = dt.year

        if bdt < 1990 or bdt > 1995:
            raise ValidationError(_("Birth Date Year should be allow between 1990 to 1995"))

        if self.age > 25 or self.age < 18:
            raise ValidationError(_("Age Should be between 18 to 25. "))

        # print temp_date[0]

        # temp_date = [x for x in self.birth_date.split('-')]
        # if temp_date[0] < '1990':

    _sql_constraints = [('email_unique', 'unique(email)', ' Please enter Unique Email id.')]