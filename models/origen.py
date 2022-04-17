# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Origen(models.Model):
    _name = 'logistica_mca.origen'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Origen'

    name = fields.Char(string='Nombre',required=True)
    direccion = fields.Char(string='Dirección',required=True)   
