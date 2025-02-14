from odoo import models, fields, api
def _group_expand_states (self, states, domain, order):
  return [key for
  key, val in type(self).service_state.selection]

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
    service_state = fields.Selection([
        ('suspenso', 'Suspenso'),
        ('posible', 'Posible aprobado'),
        ('aprobado', 'Aprobado'),
        ('sobresaliente', 'Sobresaliente'),
        ('mencion', 'Mención honorifica')
        ], string='Service Status', default='aprobado', track_visibility='always')


        

    
