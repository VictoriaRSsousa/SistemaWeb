from flask import  jsonify
from datetime import datetime 
import re

##validação de cnpj
def valida_cnpj(cnpj):
    if not (isinstance(cnpj, str) and len(cnpj) == 14 and cnpj.isdigit()):
        return {"Mensagem": "CNPJ inválido!"}
    return None

def valida_valor(valor):
    if not (isinstance(valor, (int, float)) and valor >= 0):
        return {"Mensagem": "Valor inválido!"}
    return None

def valida_descricao(descricao):
    if not (isinstance(descricao, str) and len(descricao) > 0):
        return {"Mensagem": "Descrição inválida!"}
    return None

def valida_data_vencimento(data_vencimento):
    try:
        datetime.strptime(data_vencimento, '%Y-%m-%d')
    except ValueError:
        return {"Mensagem": "Data de vencimento inválida! Formato esperado: AAAA-MM-DD"}
    return None

def valida_multa(multa):
    if not (isinstance(multa, (int, float)) and multa >= 0):
        return {"Mensagem": "Multa inválida!"}
    return None

def valida_data_pagamento(data_pagamento):
    if data_pagamento:  
        try:
            datetime.strptime(data_pagamento, '%Y-%m-%d')
        except ValueError:
            return {"Mensagem": "Data de pagamento inválida! Formato esperado: AAAA-MM-DD"}
    return None

def valida_juros(juros):
    if not (isinstance(juros, (int, float)) and juros >= 0):
        return {"Mensagem": "Juros inválido!"}
    return None
        
def valida_dados_contas_a_pagar(dados):
    valida_cnpj(dados.get('cnpj'))
    valida_valor(dados.get('valor'))
    valida_descricao(dados.get('descricao'))
    valida_data_vencimento(dados.get('data_vencimento'))
    valida_multa(dados.get('multa'))
    valida_data_pagamento(dados.get('data_pagamento'))
    valida_juros(dados.get('juros'))


def valida_nome(nome):
    if not isinstance(nome, str) or len(nome) < 3:
        return {"Mensagem": "Nome inválido! Deve conter pelo menos 3 caracteres."}
    
    
    if not re.match(r'^[a-zA-ZÀ-ÖØ-öø-ÿ\s]+$', nome):
        return {"Mensagem": "Nome inválido! Deve conter apenas letras e espaços."}
    
    return None

def valida_email(email):

    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if not isinstance(email, str) or not re.match(regex, email):
        return {"Mensagem": "E-mail inválido!"}
    
    return None

def valida_endereco(endereco):
    if not (isinstance(endereco, str) and len(endereco) > 0):
        return {"Mensagem": "endereco inválido!"}
    return None

def valida_telefone(telefone):
    if not (isinstance(telefone, (str)) and len (telefone) < 8 and telefone.isdigit()):
        return {"Mensagem": "Telefone inválido!"}
    return None

# def valida_dados_credor(dados):
#     valida_cnpj(dados.get('cnpj'))
#     valida_nome(dados.get('nome'))
#     valida_endereco(dados.get('endereco'))
#     valida_telefone(dados.get('telefone'))
#     valida_email(dados.get('email'))
