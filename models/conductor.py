# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Conductor(models.Model):
    _name = 'logistica_mca.conductor'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Conductores'

    name = fields.Char(string='Nombre', required=True, tracking=True)
    rut = fields.Char(string='Rut', tracking=True)
    tipo_licencia = fields.Selection(string='Tipo licencia', tracking=True,
                            selection=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'),
                                    ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')])
    tipo_contrato = fields.Selection(string='Tipo contrato', tracking=True,
                            selection=[('IN', 'Interno'), ('EX', 'Externo'), ('PT', 'Part-Time'), ('EE', 'Empresa')])
    telefono = fields.Char(string='Teléfono', tracking=True)
    email = fields.Char(string='email', tracking=True)