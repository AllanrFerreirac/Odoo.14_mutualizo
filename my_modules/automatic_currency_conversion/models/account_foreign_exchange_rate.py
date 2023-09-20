# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountForeignExchangeRate(models.Model):
    _name = 'account.foreign.exchange.rate'

    date = fields.Date(string='Data da taxa de câmbio', required=True)
    currency_from_id = fields.Many2one('res.currency', string='Moeda de origem', required=True)
    currency_to_id = fields.Many2one('res.currency', string='Moeda de destino', required=True)
    exchange_rate = fields.Float(string='Taxa de câmbio', required=True)