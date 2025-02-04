class Profesor(models.Model):
    _name = 'mbs_instituto.Profesor'
    _description = 'Profesores que se encuentran en el instituto'

    dni = fields.Char('DNI')
    nombre = fields.Char('Nombre')
    apellidos = fields.Char('Apellidos')
    fechaNacimiento = fields.Char('Fecha de nacimiento')
    foto = fields.Image('Foto del profesor', max_width=500, max_height=500)
    