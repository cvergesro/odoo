# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError




#Definimos modelo Biblioteca comic
class Diagnostic(models.Model):

    #Nombre y descripcion del modelo
    _name = 'hospital.diagnostic'
    _description = 'Diagnostic'

    _rec_name = 'pacient'
    pacient= fields.Char('Pacient')
    metge = fields.Many2one('hospital.metge', string='Metges')
    diagnostic= fields.Char('Diagnostic')
    
