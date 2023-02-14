# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError




#Definimos modelo Biblioteca comic
class Prestar(models.Model):

    #Nombre y descripcion del modelo
    _name = 'biblioteca.comic.prestar'
    _description = 'Prestar'

    _rec_name = 'nombre'


    #Atributo nombre
    nombre = fields.Many2one('biblioteca.comic', string='Comic')
    socio= fields.One2many('biblioteca.comic.gestionarsocios', 'id_socio', string='Prestado a: ')
    
    fecha_prestamo = fields.Date('Fecha prestamo')
    fecha_devolucion = fields.Date('Fecha devolucion')

    @api.constrains('fecha_prestamo')
    def _check_release_date(self):
        # Recorremos el modelo
        for record in self:

            if record.fecha_prestamo and record.fecha_prestamo > fields.Date.today():
                
                raise models.ValidationError('La fecha de prestamo debe ser anterior a la actual')

    @api.constrains('fecha_devolucion')
    def _check_devolucion(self):
        # Recorremos el modelo
        for record in self:
            if record.fecha_devolucion and record.fecha_devolucion > fields.Date.today():
                raise models.ValidationError('La fecha de devolucion debe ser posterior a la actual')



