# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TiposTraslado(models.Model):
    _name = 'logistica_mca.tipos.traslado'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tipos de Traslado'

    name = fields.Char(string='Indentificación', required=True, tracking=True)
