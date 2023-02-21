# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Pacient(models.Model):
    #Nombre y descripcion del modelo
    _name = 'hospital.pacient'
    _description = 'Pacients hospital'



    #Atributos del modelo


    _rec_name = 'nom'

    #Nombre categoria
    nom = fields.Char('Nom')
    cognoms = fields.Char('Cognoms')
    simptomes=fields.Many2many('res.partner', string='Simptomes')

