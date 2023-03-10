# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class CicleFormatiu(models.Model):

    #Nombre y descripcion del modelo
    _name = 'cicle.formatiu.profesor'

    _description = 'Profesors'

    _rec_name = 'nom'


    nom = fields.Char('Nom i Cognoms', required=True, index=True)
    departament = fields.Char('Departament')
    any = fields.Integer('Any de naixement')
    titulacio = fields.Char('Titulació')
    moduls=fields.One2many('cicle.formatiu.modul', 'profesor', string='Moduls impartits')
    imatge= fields.Binary('Foto')