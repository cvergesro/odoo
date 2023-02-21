# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Metge(models.Model):
   
    _name = 'hospital.metge'
    _description = 'Metges'


    _rec_name = 'nom'


    nom = fields.Char('Nom')
    cognom = fields.Char('Cognom')
    num_colegiat = fields.Many2one('hospital.diagnostic', string='Número col·legiat')


