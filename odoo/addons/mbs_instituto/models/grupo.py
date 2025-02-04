from odoo import models, fields, api

class Grupo(models.Model):
    _name = 'mbs_instituto.grupo'
    _description = 'Grupos en los cuales se matriculan los alumnos'

    nombre = fields.Char('Nombre')
    curso = fields.Integer('Curso')
    