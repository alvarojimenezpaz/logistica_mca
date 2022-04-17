# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TiposSiniestro(models.Model):
    _name = 'logistica_mca.tipos.siniestro'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tipos de Siniestro'

    name = fields.Char(string='Indentificación', required=True, tracking=True)
