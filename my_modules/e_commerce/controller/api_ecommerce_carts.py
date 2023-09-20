# -*- coding: utf-8 -*-
'''
####################################################################################################################
OBS.: 
    Nao foi feito rota para excluir registro, pois a regra de negocio nao permite.
####################################################################################################################    
''' 

import json
from odoo import http
from odoo.http import request, Response

class ApiController(http.Controller):

    @http.route('/api/carts', type='http', auth='none', methods=['GET'])
    def get_carts(self):
        """
            Rota para retornar todos os carrinhos
        """
        carts = request.env['cart'].sudo().search([])
        cart_data = []
        for cart in carts:
            cart_data.append({
                'id': cart.id,
                'cod': cart.cod,
                'total_order': cart.total_order,
                'state': cart.state,
            })
        return Response(json.dumps(cart_data), content_type='application/json')
    
    @http.route('/api/carts', type='json', auth='none', methods=['POST'])
    def create_cart(self, **params):
        """
            Rota para criar um carrinho
        """
        if not params:
            return {'error': 'Parametro nao providenciado'}
        
        product_ids = params.get('product_ids', [])
        if not product_ids:
            return {'error': 'IDs dos produtos nao providenciado'}
        
        cart = request.env['cart'].sudo().create({'product_ids': product_ids})
        return {
            'message': 'Carrinho criado com sucesso', 
            'cart_id': cart.id
        }
    
    @http.route('/api/carts/', type='json', auth='none', methods=['PUT'])
    def update_cart(self, **params):
        """
            Rota para editar um carrinho
        """
        cart = request.env['cart'].sudo().browse(params.get('cart_id'))
        if not cart:
            return {'error': 'Carrinho nao encontrado'}
        
        if not params:
            return {'error': 'Parametro nao providenciado'}
        
        product_ids = params.get('product_ids', [])
        if not product_ids:
            return {'error': 'IDs dos produtos nao informado'}
        
        cart.write({'product_ids': [(6, 0, product_ids)]})
        return {
            'message': 'Carrinho editado com Sucesso'
        }
