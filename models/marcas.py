# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Marca(models.Model):
    _name = 'logistica_mca.marcas'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Marcas de Vehículos'

    name = fields.Char(string='Marca de vehículo',required=True, tracking=True)
