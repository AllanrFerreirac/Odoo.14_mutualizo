# -*- coding: utf-8 -*-

from odoo import models, fields, api
from ..contants import CARD_STATUS, ORDER_STATUS

class Order(models.Model):
    _name = 'order'
    _rec_name = 'cod'
    
    cod = fields.Char(string=u'Codigo do carrinho')
    product_ids = fields.Many2many('product', string=u'Produtos')
    total_order = fields.Float(string=u'Total do Pedido')
    state = fields.Selection(ORDER_STATUS, default='pending') 