# Prova Desenvolvedor Odoo - Allan Rogerio Ferreira da Costa

Arquivoos da prova de desenvolvedor Odoo onde contem codigo Python e Odoo, incluindo algoritmos, modelagem de sistemas orientados a objetos, e conhecimentos específicos nos módulos de contabilidade e contas a pagar do Odoo. Contem modulos customizados com heranca e criacao de modulos


## Tabela de Conteúdo

- [Instalação](#instalação)
- [Uso](#uso)
- [Observacao](*Observacao)

## Instalação

Instalar o docker
Abrir o terminar e caminhar ate a pasta do projeto onde esta os arquivos
Rodar o comando do docker onde tem a imagem do Odoo.14 e as configuracoes necessarias: 
* docker compose up -d
Rodar o comando para ver se esta em processo o banco de dados e o Odoo:
* docker ps

# Uso
acessar:
* localhost:8069 
Assim tera acesso ao painel do Odoo e podera fazer uma base com login e senha
Fazer a instalacao dos modulos
- E-Commerce
- Conversao Automatica de Moeda
- Integração de Fatura de Conta

# Observacao

Foi usado o Odoo na versao 14
Na versao 14 o modulo account.invoice foi substituido pelo modulo account.move
