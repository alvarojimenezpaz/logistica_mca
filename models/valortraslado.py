# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Valortraslado(models.Model):
    _name = 'logistica_mca.valortraslado'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Valor Origen -> Destino'

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s -> %s | %s" % (record.origen_id.name, record.destino_id.name, record.tipo_traslado.name)
            result.append((record.id, rec_name))
        return result

    name = fields.Char(string='Origen -> Destino')
    origen_id = fields.Many2one('logistica_mca.origen',string='Origen', required=True)
    destino_id = fields.Many2one('logistica_mca.destino',string='Destino', required=True)
    tipo_traslado = fields.Many2one('logistica_mca.tipos.traslado', string='Tipo Traslado', required=True)
    valor = fields.Float(string='Valor', required=True, default=0)
    valor_uf = fields.Float(string='UFs', required=True, default=0)

    @api.model
    def _default_currency_id(self):
        value = self.env['res.currency'].search([('name', '=', 'CLP')], limit=1)
        return value and value.id or False

    currency_id = fields.Many2one('res.currency', string='Moneda', default=_default_currency_id)
