# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TiposRendicion(models.Model):
    _name = 'logistica_mca.tipos.rendicion'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tipos de rendiciones'

    name = fields.Char(string='Indentificación', required=True, tracking=True)
    tipo = fields.Selection(string='Tipo', selection=[('gasto', 'Gasto'), ('ingreso', 'Ingreso')], tracking=True,
                            required=True, default='gasto')
