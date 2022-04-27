# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Solicita(models.Model):
    _name = 'logistica_mca.solicita'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'solicita'

    name = fields.Char(string='Nombre',required=True, tracking=True)
