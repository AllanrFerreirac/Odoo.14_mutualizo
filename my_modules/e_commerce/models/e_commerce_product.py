# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product(models.Model):
    _name = 'product'
    _rec_name = 'name'
    
    name = fields.Char(string=u'Nome')
    price = fields.Float(string=u'Preço')
    stock = fields.Integer(string=u'Estoque')
    
   