# -*- coding: utf-8 -*-

import requests
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        '''
            Metodo que herda o metodo original do botão "Confirmar" do account.move e chama um metodo passando um parametro 
            para se comunicar com uma API externa.
        '''
        result = super(AccountMove, self).action_post()
        for move in self:
            if move.state == 'posted':
                self.account_api_external(move)
        return result
    
    def account_api_external(self, move):
        '''
            Metodo que recebe um parametro e faz a comunicação com uma API externa e entrega um dicionario de chaves e valores,
            dependendo a resposta da API, chama um metodo passando quatro parametros
            parametro que recebe: objeto account.move
        '''
        api_url = 'URL_API_EXTERNAL'

        data_to_send = {
            'invoice_number': move.name,
            'total_amount': move.amount_total,
            'customer_name': move.partner_id.name,
            'customer_email': move.partner_id.email,
            'invoice_date': move.invoice_date,
            'due_date': move.invoice_date_due,
            'invoice_lines': [],
        }

        for line in move.invoice_line_ids:
            line_data = {
                'product_name': line.product_id.name,
                'quantity': line.quantity,
                'price_unit': line.price_unit,
                'subtotal': line.price_subtotal,
            }
            data_to_send['invoice_lines'].append(line_data)

        try:
            response = requests.post(api_url, json=data_to_send)
            if response.status_code == 200:
                status = 'success'
                response_message = 'Fatura enviada com sucesso!.'
                self.create_move_integration(move, response, status, response_message)
                return
            else:
                status = 'error'
                response_message = f'Erro na comunicação com a API externa!'
                self.create_move_integration(move, response, status, response_message)
                return
        except Exception as e:
            status = 'error'
            response_message = f'Erro na comunicação com a API externa: {str(e)}'
            self.create_move_integration(move, response, status, response_message)
            return

    def create_move_integration(self, move, response, status, response_message): 
        '''
            Metodo que recebe quatro parametros e faz a criacao do objeto account.move.integration
            parametro que recebe: objeto account.move
                                  resposta da API externa
                                  status da resposta da API
                                  messagem de erro
        '''  
        dict_move_integration = {
            'invoice_id': move.id,
            'external_system_id': response.get('id'),
            'status': status,
            'response_message': response_message,
        }
        self.env['account.move.integration'].create(dict_move_integration)
        return