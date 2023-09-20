# -*- coding: utf-8 -*-
{
    'name': 'Integração de Fatura de Conta',
    'version': '1.0',
    'category': '',
    'description': """
Modulo de integracao do modulo de faturas e contas.
===================================================
""",
    'depends': [
        'base',
        'account',
        ],
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_integration.xml',
    ],
    'license': 'LGPL-3',
}

