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

    @http.route('/api/products', type='http', auth='none', methods=['GET'])
    def get_products(self):
        """
            Rota para retornar todos os produtos
        """
        products = request.env['product'].sudo().search([])
        product_data = []
        for product in products:
            product_data.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'stock': product.stock,
            })
        return Response(json.dumps(product_data), content_type='application/json')
    
    @http.route('/api/products', type='json', auth='none', methods=['POST'])
    def create_product(self, **params):
        """
            Rota para criar um produto
        """
        product = request.env['product'].sudo().create({
            'name': params.get('name'),
            'price': params.get('price'),
            'stock': params.get('stock'),
        })
        return {
            'message': 'Produto criado com sucesso',
            'product_id': product.id,
        }
        
    @http.route('/api/products', type='json', auth='none', methods=['PUT'])
    def update_cart(self, **params):
        """
            Rota para editar um carrinho
        """
        product = request.env['product'].sudo().browse(params.get('product_id'))
        if not product:
            return {'error': 'Produto nao encontrado'}
        
        if not params:
            return {'error': 'Parametros nao providenciados'}

        dict_product = {
            'name': params.get('name'),
            'price': params.get('price'),
            'stock': params.get('stock'),
        }
        product.write(dict_product)
        return {
            'message': 'Produto editado com sucesso'
        }