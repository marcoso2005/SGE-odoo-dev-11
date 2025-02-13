from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'mbs_instituto.alumno'
    _description = 'Alumnos que se encuentran matriculados en el instituto'

    dni = fields.Char('DNI')    
    numEstudiante = fields.Char('Número de estudiante')
    name = fields.Char('Nombre')
    apellidos = fields.Char('Apellidos')
    fechaNacimiento = fields.Date('Fecha de nacimiento')
    repetidor = fields.Boolean('Repetidor')
    media = fields.Float('Media del curso')
    foto = fields.Image('Foto del alumno', max_width=100, max_height=100)
