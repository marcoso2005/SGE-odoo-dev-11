from odoo import models, fields, api

class Asignatura(models.Model):
    _name = 'mbs_instituto.asignatura'
    _description = 'Asignaturas a impartir en los diversos grados'

    nombre = fields.Char('Nombre')
    horas = fields.Integer('Horas de la asignatura')
    