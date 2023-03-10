# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class Modul(models.Model):

    #Nombre y descripcion del modelo
    _name = 'cicle.formatiu.modul'

    _description = 'Mòduls'

    _rec_name = 'nom'


    #Atributo nombre
    nom = fields.Char('Nom del mòdul', required=True, index=True)
    cicle = fields.Many2one('cicle.formatiu', string='Cicle al que pertany el mòdul')
    profesor=fields.Many2one('cicle.formatiu.profesor', string='Profesor que imparteix el mòdul')
    curs=fields.Selection(
        [('primer', 'Primer'),
         ('segon', 'Segon')],
        'Curs', default="primer")
    hores=fields.Integer('Hores de Duració')