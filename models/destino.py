# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Destino(models.Model):
    _name = 'logistica_mca.destino'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Destino'

    name = fields.Char(string='Nombre',required=True, tracking=True)
    direccion = fields.Char(string='Dirección',required=True, tracking=True)
