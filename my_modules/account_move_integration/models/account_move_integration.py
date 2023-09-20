# -*- coding: utf-8 -*-

from odoo import models, fields
from ..contants import INTEGRATION_STATUS

class AccountMoveIntegration(models.Model):
    _name = 'account.move.integration'
    
    invoice_id = fields.Many2one('account.move', string='Fatura')
    external_system_id = fields.Char(string=u"ID do sistema externo")
    status = fields.Selection(INTEGRATION_STATUS ,string=u"Status da integração", default='pending')
    response_message = fields.Text(string=u"Mensagem de resposta")
    