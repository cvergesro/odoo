# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class Alumne(models.Model):

    #Nombre y descripcion del modelo
    _name = 'cicle.formatiu.alumne'

    _description = 'Alumnes'

    _rec_name = 'nom'


    #Atributo nombre
    nom = fields.Char('Nom i Cognoms', required=True, index=True)
    any = fields.Integer('Any de naixement')
    cicle = fields.Char('Cicle Formatiu')
    curs=fields.Selection(
        [('primer', 'Primer'),
         ('segon', 'Segon'),
         ('altre','Altre')],
        'Curs', default="primer")
    moduls_matriculats=fields.Many2many('res.partner', string='Moduls matriculats')
    imatge= fields.Binary('Foto')