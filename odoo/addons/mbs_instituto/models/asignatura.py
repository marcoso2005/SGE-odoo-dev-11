class Asignatura(models.Model):
    _name = 'mbs_instituto.Asignaturas'
    _description = 'Asignaturas a impartir en los diversos grados'

    nombre = fields.Char('Nombre')
    horas = fields.Integer('Horas de la asignatura')
    