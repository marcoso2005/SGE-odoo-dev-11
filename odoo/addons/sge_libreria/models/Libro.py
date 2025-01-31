from odoo import models, fields, api

class Libro(models.Model):
   _name = 'sge_libreria.libro'
   _description = 'Libro'

   name = fields.Char('Nombre')
   precio = fields.Float('Precio')
   ejemplares = fields.Integer('Ejemplares')
   fecha_compra = fields.Date('Fecha compra')
   segmano = fields.Boolean('Segmano')
   estado = fields.Selection([
      ('0', 'Malo'),
      ('1', 'Regular'),
      ('2', 'Bueno')
   ], string='Estado', default='0')

   # malo regular bueno


