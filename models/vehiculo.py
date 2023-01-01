# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Vehiculo(models.Model):
    _name = 'logistica_mca.vehiculo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Vehículos'

    name = fields.Char(string='Vehículo', compute="_compute_vehicle_name", tracking=True)
    vin = fields.Char(string='VIN', required=True, tracking=True)
    patente = fields.Char(string='Patente', tracking=True)
    agno = fields.Integer(string='Año', tracking=True)
    marcas_id = fields.Many2one('logistica_mca.marcas',string='Marca', required=True, tracking=True)
    modelos_id = fields.Many2one('logistica_mca.modelos',string='Modelo', required=True, tracking=True)

    @api.depends('marcas_id.name', 'modelos_id.name')
    def _compute_vehicle_name(self):
        for record in self:
            record.name = (record.marcas_id.name or '') + ', ' + (record.modelos_id.name or '') + ', VIN ' + (record.vin or '') + ', PT ' + (record.patente or '')
