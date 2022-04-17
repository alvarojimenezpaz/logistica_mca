# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Rendicion(models.Model):
    _name = 'logistica_mca.rendicion'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Rendición de Gastos'

    @api.depends('rendicion_line.valor_real_line')
    def _amount_all(self):
        valor = 0
        for rendicion in self:
            for line in rendicion.rendicion_line:
                valor += line.valor_real_line

            rendicion.update({'valor_total': valor})

    name = fields.Char(string='Rendición', required=True, copy=False, index=True, default='New', tracking=True)
    fecha = fields.Date(string='Fecha', required=True, tracking=True)
    nombre = fields.Char(string='Nombre', tracking=True)
    nro_talonario = fields.Char(string='Nro.Talonario', tracking=True)
    valor_total = fields.Float(string='Total', store=True, readonly=True, compute='_amount_all')
    rendicion_line = fields.One2many('logistica_mca.rendicion.line', 'rendicion_id', string='Detalle rendición',
                                     tracking=True, required=True)
    traslado_id = fields.Many2many('logistica_mca.traslado', string='Traslado')

    @api.model
    def _default_currency_id(self):
        value = self.env['res.currency'].search([('name', '=', 'CLP')], limit=1)
        return value and value.id or False

    currency_id = fields.Many2one('res.currency', string='Moneda', default=_default_currency_id)

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('logistica_mca.rendicion') or ('New')
        result = super(Rendicion, self).create(vals)
        return result


class RendicionLine(models.Model):
    _name = 'logistica_mca.rendicion.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Detalle Rendición de Gastos'
    _order = 'rendicion_id, fecha'

    @api.depends('valor')
    def _valor_real_line(self):
        for line in self:
            if line.tiposrendicion_id.tipo == 'gasto':
                line.valor_real_line = (line.valor * -1)
            else:
                line.valor_real_line = (line.valor)
        return line.valor_real_line

    rendicion_id = fields.Many2one('logistica_mca.rendicion', string='Rendición', tracking=True, required=True)
    fecha = fields.Date('Fecha', related='rendicion_id.fecha', store=True, readonly=True)
    nro_talonario = fields.Char('Nro.Talonario', related='rendicion_id.nro_talonario', readonly=True)
    nombre = fields.Char('Nombre', related='rendicion_id.nombre', readonly=True)
    tiposrendicion_id = fields.Many2one('logistica_mca.tipos.rendicion', string='Tipo', tracking=True, required=True)
    tipo_doc = fields.Selection(string='Tipo Doc', selection=[('FAC', 'Factura'), ('BOL', 'Boleta'), ('VOU', 'Voucher')],
                                tracking=True)
    nro_doc = fields.Char(string='Nro.Doc', tracking=True)
    fecha_doc = fields.Date(string='Fec.Doc', tracking=True)
    valor = fields.Float(string='Valor', tracking=True, required=True, default=0)
    valor_real_line = fields.Float(string='Valor Real', store=True, readonly=True, compute='_valor_real_line')

    @api.model
    def _default_currency_id(self):
        value = self.env['res.currency'].search([('name', '=', 'CLP')], limit=1)
        return value and value.id or False

    currency_id = fields.Many2one('res.currency', string='Moneda', default=_default_currency_id)
