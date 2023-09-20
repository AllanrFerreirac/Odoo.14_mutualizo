# -*- coding: utf-8 -*-
{
    'name': 'E-Commerce ',
    'version': '1.0',
    'category': '',
    'description': """
Modulo de e-commerce com tabelas Produto, Carrinho e Pedido.
===================================================
""",
    'depends': [
        'base'
        ],
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/order_views.xml',
        'views/cart_views.xml',
    ],
    'license': 'LGPL-3',
}

