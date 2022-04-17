# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Modelo(models.Model):
    _name = 'logistica_mca.modelos'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Modelos de Vehículos'

    name = fields.Char(string='Nombre Modelo',required=True)
    marcas_id = fields.Many2one('logistica_mca.marcas', string='Marca', tracking=True, required=True)
