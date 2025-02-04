class Grupo(models.Model):
    _name = 'mbs_instituto.Grupo'
    _description = 'Grupos en los cuales se matriculan los alumnos'

    nombre = fields.Char('Nombre')
    curso = fields.Integer('Curso')
    