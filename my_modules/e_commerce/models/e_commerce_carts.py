# -*- coding: utf-8 -*-

from odoo import models, fields, api
from ..contants import CARD_STATUS

class Cart(models.Model):
    _name = 'cart'
    _rec_name = 'cod'
    
    cod = fields.Char(string=u'Codigo')
    product_ids = fields.Many2many('product', string=u'Produtos')
    total_order = fields.Float(string=u'Total', compute='_compute_total')
    state = fields.Selection(CARD_STATUS, default='in_progress')
    
    @api.depends('product_ids')
    def _compute_total(self):
        """Metodo para calcular os valores do produtos selecionado"""
        for cart in self:
            cart.total_order = sum(product.price for product in cart.product_ids)
    
    @api.model
    def create(self, vals):
        """Metodo para criar o carrinho e colocar um codigo para o mesmo"""
        result = super(Cart, self).create(vals)
        cart = self.env['cart'].search([])
        result.cod = 'CODIGO CARRINHO - 00' + str(len(cart))
        return result
    
    def cancel_purchase(self):
        """Metodo para cancelar o carrinho"""
        self.state = 'cancel_purchase'
    
    def finalize_purchase(self):
        """Metodo para finalizar o carrinho e fazer a criacao do pedido"""
        dict_create = {
            'cod': self.cod,
            'total_order': self.total_order,
        }
        order_create = self.env['order'].create(dict_create)
        for product in self.product_ids:
            order_create.product_ids |= product
        self.state = 'finished'  