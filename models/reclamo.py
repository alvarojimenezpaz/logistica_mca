# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reclamo(models.Model):
    _name = 'logistica_mca.reclamo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Reclamos'

    @api.depends('reclamo_line.valor')
    def _amount_all(self):
        valor = 0
        for reclamo in self:
            for line in reclamo.reclamo_line:
                valor += line.valor

            reclamo.update({'valor_total': valor})

    name = fields.Char(string='Reclamo', required=True, copy=False, index=True, default='New', tracking=True)
    fecha = fields.Date(string='Fecha', required=True, tracking=True)
    nombre = fields.Char(string='Nombre', tracking=True)
    tipo_reclamo_id = fields.Many2one('logistica_mca.tipos.reclamo', string='Tipo de Reclamo')
    valor_total = fields.Float(string='Total', store=True, readonly=True, compute='_amount_all')
    reclamo_line = fields.One2many('logistica_mca.reclamo.line', 'reclamo_id', string='Detalle reclamo',
                                     tracking=True, required=True)
    traslado_id = fields.Many2many('logistica_mca.traslado', string='Traslado')
    observacion = fields.Text(string='Notas', tracking=True)

    @api.model
    def _default_currency_id(self):
        value = self.env['res.currency'].search([('name', '=', 'CLP')], limit=1)
        return value and value.id or False

    currency_id = fields.Many2one('res.currency', string='Moneda', default=_default_currency_id)

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('logistica_mca.reclamo') or ('New')
        result = super(Reclamo, self).create(vals)
        return result


    class ReclamoLine(models.Model):
        _name = 'logistica_mca.reclamo.line'
        _inherit = ['mail.thread', 'mail.activity.mixin']
        _description = 'Detalle Reclamo'
        _order = 'reclamo_id, fecha'

        reclamo_id = fields.Many2one('logistica_mca.reclamo', string='Reclamo', tracking=True, required=True)
        fecha_reclamo = fields.Date('Fecha Reclamo', related='reclamo_id.fecha', store=True, readonly=True)
        tipo_reclamo = fields.Many2one(related='reclamo_id.tipo_reclamo_id', string='Tipo Reclamo',  store=True, readonly=True)
        tipo_siniestro_id = fields.Many2one('logistica_mca.tipos.siniestro', string='Tipo Siniestro')
        nro_siniestro = fields.Char(string='Nro.Siniestro', required=True, tracking=True)
        fecha = fields.Date(string='Fecha Siniestro', required=True, tracking=True)
        valor = fields.Float(string='Valor', tracking=True)
        deducible = fields.Boolean(string='Deducible', tracking=True)
        observacion = fields.Text(string='Notas', tracking=True)

        @api.model
        def _default_currency_id(self):
            value = self.env['res.currency'].search([('name', '=', 'CLP')], limit=1)
            return value and value.id or False

        currency_id = fields.Many2one('res.currency', string='Moneda', default=_default_currency_id)
