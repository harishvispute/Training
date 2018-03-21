from odoo import models, fields , api, _


class Hospital(models.Model):
    _name = 'hospital.hospital'

    name = fields.Char('Hospital Name', required=True)
    hadd = fields.Text('Address')
    phone = fields.Char('Phone')
    doctor_ids = fields.Many2many('doctor.doctor', string='Doctors')
    # start_date = fields.Date('Start Date')


class Doctor(models.Model):
    _name = 'doctor.doctor'

    name = fields.Char('Doctor Name', required=True)
    designation = fields.Char('Designation')
    hospital_ids = fields.Many2many('hospital.hospital', string='Hospitals')
    # department_id = fields.Many2one('department.department',"Department")
    # patient_ids = fields.Many2many('patient.patient','patient_doctor_rel','p_id','d_id', string='patients')



class Department(models.Model):
    _name = 'department.department'

    name = fields.Char('Department Name', required=True)


class Patient(models.Model):
    _name = 'patient.patient'

    name = fields.Char('Patient_Name', required=True)
    add = fields.Text('Address')
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Others')], "Gender", default='m')
    age = fields.Integer('Age')
    diagnosis = fields.Char('Diagnosis')

    # hospital_id = fields.Many2one('hospital.hospital','Hospital')


    # doctor_ids = fields.Many2many('doctor.doctor', 'patient_doctor_rel', 'p_id', 'd_id', string='Doctor')
    # color = fields.Integer('Color Index')
    # admit_date = fields.Date('Admit Date')
    # discharge_date = fields.Date('Discharge Date')
    # report = fields.Boolean('Did you have any report ..?')

    # @api.multi
    # def change_male(self):
    #     self.gender = 'm'
    #
    # @api.multi
    # def change_female(self):
    #     self.gender = 'f'
    #
    # @api.multi
    # def change_other(self):
    #     self.gender = 'o'



