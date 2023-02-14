# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class GestionarSocis(models.Model):
   
    _name = 'biblioteca.comic.gestionarsocios'
    _description = 'Gestionar Socios'


    _rec_name = 'nombre'


    nombre = fields.Char('Nombre')


    apellido = fields.Char('Apellidos')
    
    id_socio = fields.Many2one('biblioteca.comic.prestar', string='Id socio')


