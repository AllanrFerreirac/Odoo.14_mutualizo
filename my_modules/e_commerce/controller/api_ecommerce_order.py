# -*- coding: utf-8 -*-
'''
####################################################################################################################
OBS.: 
    Nao foi feito rota para criar,editar e excluir registro, pois a regra de negocio nao permite.
####################################################################################################################    
''' 

import json
from odoo import http
from odoo.http import request, Response

class ApiController(http.Controller):

    @http.route('/api/orders', type='http', auth='none', methods=['GET'])
    def get_orders(self):
        """
            Rota retornar todos os pedidos
        """
        orders = request.env['order'].sudo().search([])
        order_data = []
        for order in orders:
            order_data.append({
                'id': order.id,
                'cod': order.cod,
                'total_order': order.total_order,
                'state': order.state,
            })
        return Response(json.dumps(order_data), content_type='application/json')
