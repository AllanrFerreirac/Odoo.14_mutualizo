# -*- coding: utf-8 -*-
{
    'name': 'Conversao Automatica de Moeda',
    'version': '1.0',
    'category': '',
    'description': """
Modulo de conversao automatica de moeda.
===================================================
""",
    'depends': [
        'base',
        'account',
        ],
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/account_foreign_exchange_rate.xml',
    ],
    'license': 'LGPL-3',
}

