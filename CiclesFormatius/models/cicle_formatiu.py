# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class CicleFormatiu(models.Model):

    #Nombre y descripcion del modelo
    _name = 'cicle.formatiu'

    _description = 'Cicles Formatius'

    _rec_name = 'nom'


    #Atributo nombre
    nom = fields.Char('Nom', required=True, index=True)
    tipus = fields.Char('Familia Profesional')
    moduls=fields.One2many('cicle.formatiu.modul', 'cicle', string='Moduls')
    grau=fields.Selection(
        [('mitja', 'Grau mitja'),
         ('superior', 'Grau superior')],
        'Grau', default="mitja")  
    descripcio=fields.Html('Descripció', sanitize=True, strip_style=False)