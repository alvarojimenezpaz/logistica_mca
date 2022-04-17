# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TiposReclamo(models.Model):
    _name = 'logistica_mca.tipos.reclamo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tipos de Reclamo'

    name = fields.Char(string='Indentificación', required=True, tracking=True)
