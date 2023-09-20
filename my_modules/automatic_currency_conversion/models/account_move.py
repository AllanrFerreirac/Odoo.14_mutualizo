# -*- coding: utf-8 -*-
'''
####################################################################################################################
OBS.: 
    Verifiquei que requisicao apenas pede para calcular o valor final porem nas linhas do objeto account.move.line
    existe um campo sub total que calcula o valor com a quantidade do produto, porem nao foi feito essa logica pois
    a requisicao so pede para fazer do calculo final.
####################################################################################################################    
''' 

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    currency_id = fields.Many2one('res.currency', string='Moeda de transação')
    
    def validation_currency_id(self):
        '''
            Metodo para validar se existe taxa de câmbio cadastrada
        '''
        if self.currency_id and self.currency_id != self.company_id.currency_id:
            exchange_rate = self.env['account.foreign.exchange.rate'].search([
                ('currency_from_id', '=', self.currency_id.id),
                ('currency_to_id', '=', self.company_id.currency_id.id),
                ('date', '=', self.date),
            ], limit=1)
            return exchange_rate
    
    @api.onchange('currency_id')
    def onchange_currency_id(self):
        '''
            Metodo que chama uma validacao, caso retorne False apresenta um erro
        '''
        if not self.validation_currency_id():
            return {
                'warning': {
                    'title': 'Aviso',
                    'message': 'Não foi encontrada uma taxa de câmbio para a data selecionada. A conversão não é possível.',
                },
            }
    
    def _compute_amount(self):
        '''
            Metodo computado, herdado do model account.move e aplicado uma logica para colocar o valor correto
        '''
        super(AccountMove, self)._compute_amount()
        exchange_rate = self.validation_currency_id()
        if exchange_rate:
            self.amount_total = self.amount_total / exchange_rate.exchange_rate
                         