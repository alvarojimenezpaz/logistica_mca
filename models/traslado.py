# -*- coding: utf-8 -*-

#from tokenize import String
from odoo import models, fields, api


class Traslado(models.Model):
    _name = 'logistica_mca.traslado'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Traslado de Vehículo'

    @api.onchange('valortraslado_id')
    def _onchange_valortraslado_id(self):
        for line in self:
            if line.valortraslado_id:
                line.valor = line.valortraslado_id.valor
                line.valor_uf = line.valortraslado_id.valor_uf

    @api.depends('adicional_id.valor')
    def _amount_adicionales(self):
        valor = 0
        for traslado in self:
            for line in traslado.adicional_id:
                valor += line.valor

        traslado.update({'valor_adicionales': valor})

    @api.depends('comision_id.valor')
    def _amount_comisiones(self):
        valor = 0
        for traslado in self:
            for line in traslado.comision_id:
                valor += line.valor

        traslado.update({'valor_comisiones': valor})


    name = fields.Char(string='Traslado', required=True, copy=False, index=True, default='New')
    state = fields.Selection([
        ("new","New"),
        ("ingresado","Ingresado"),
        ("asignado","Asignado"),
        ("transito", "En Transito"),
        ("entregado", "Entregado"),
        ("verificado", "Verificado"),
        ("facturado", "Facturado"),
        ("cancelado", "Cancelado"),
    ], default="new", string="Estado")
    guia = fields.Char(string="N° Guía", required=True, default=0)
    pedido = fields.Char(string="N° Pedido", required=True, default=0)
    hes = fields.Char(string="N° HES", required=True, default=0)
    fecha = fields.Date(string='Fecha', required=True, tracking=True)
    solicita = fields.Many2one('logistica_mca.solicita', string='Solicita', required=True)
    conductor = fields.Many2one('logistica_mca.conductor', string='Conductor', required=True)
    tipo_traslado = fields.Many2one('logistica_mca.tipos.traslado', string='Tipo Traslado', required=True)
    cliente = fields.Many2one('res.partner', string='Cliente', required=True)
    vehiculo_id = fields.Many2one('logistica_mca.vehiculo', string='Vehículo', required=True)
    #marcas_id = fields.Many2one('logistica_mca.marcas',string='Marca', required=True)
    #modelos_id = fields.Many2one('logistica_mca.modelos',string='Modelo', required=True)
    #vin = fields.Char(string='VIN', required=True,  tracking=True)
    valortraslado_id = fields.Many2one('logistica_mca.valortraslado', string='Origen -> Destino', required=True)
    valor = fields.Float(string='Valor', tracking=True)
    valor_uf = fields.Float(string='UFs', tracking=True)
    factura = fields.Char(string="N° Factura", required=True, default=0)
    #------------------------------------------------------------------------------------------------------
    rendicion_id = fields.Many2many('logistica_mca.rendicion', string='Rendición')
    valor_rendiciones = fields.Float('Rendiciones', related='rendicion_id.valor_total', readonly=True)
    #------------------------------------------------------------------------------------------------------
    reclamo_id = fields.Many2many('logistica_mca.reclamo', string='Reclamo')
    valor_reclamos = fields.Float('Reclamos', related='reclamo_id.valor_total', readonly=True )
    #------------------------------------------------------------------------------------------------------
    adicional_id = fields.One2many('logistica_mca.traslado.adicional', 'traslado_id', string='Detalle Adicional',
                                  tracking=True, required=True)
    valor_adicionales = fields.Float(string='Adicionales', store=True, readonly=True, compute='_amount_adicionales')
    #------------------------------------------------------------------------------------------------------
    comision_id = fields.One2many('logistica_mca.traslado.comision', 'traslado_id', string='Detalle Comisión',
                                     tracking=True, required=True)
    valor_comisiones = fields.Float(string='Comisiones', store=True, readonly=True, compute='_amount_comisiones')
    #------------------------------------------------------------------------------------------------------


    @api.model
    def _default_currency_id(self):
        value = self.env['res.currency'].search([('name', '=', 'CLP')], limit=1)
        return value and value.id or False

    currency_id = fields.Many2one('res.currency', string='Moneda', default=_default_currency_id)

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('logistica_mca.traslado') or ('New')
        result = super(Traslado, self).create(vals)
        return result

class TrasladoAdicional(models.Model):
    _name = 'logistica_mca.traslado.adicional'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Detalle de Adicionales en Traslado'

    traslado_id = fields.Many2one('logistica_mca.traslado', string='Lineas de Adicional', tracking=True,
                                   required=True)
    name = fields.Char(string='Descripción', tracking=True, required=True)
    valor = fields.Float(string='Valor', tracking=True, required=True, default=0)

    @api.model
    def _default_currency_id(self):
        value = self.env['res.currency'].search([('name', '=', 'CLP')], limit=1)
        return value and value.id or False

    currency_id = fields.Many2one('res.currency', string='Moneda', default=_default_currency_id)


class TrasladoComision(models.Model):
    _name = 'logistica_mca.traslado.comision'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Detalle de Comisiones en Traslado'

    traslado_id = fields.Many2one('logistica_mca.traslado', string='Lineas de Comisión', tracking=True,
                                   required=True)
    name = fields.Char(string='Descripción', tracking=True, required=True)
    valor = fields.Float(string='Valor', tracking=True, required=True, default=0)

    @api.model
    def _default_currency_id(self):
        value = self.env['res.currency'].search([('name', '=', 'CLP')], limit=1)
        return value and value.id or False

    currency_id = fields.Many2one('res.currency', string='Moneda', default=_default_currency_id)
