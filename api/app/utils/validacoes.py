from flask import  jsonify
from datetime import datetime 
import re

##validação de cnpj
def valida_cnpj(cnpj):
    pattern = r'^(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}|\d{14})$'
    if not re.match(pattern, cnpj):
        return {"Mensagem": "CNPJ inválido!"}
    return None

def valida_valor(valor):
    if not isinstance(valor, (int, float)):  
        print("nao é numero")
        return {"Mensagem": "Valor inválido!"}   
    if valor < 0:  
        return {"Mensagem": "Valor inválido!"}
    
    return None

def valida_status(status):
    if not (isinstance(status, str)):
        return {"Mensagem": "Status inválida!"}
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
    erro = valida_cnpj(dados.get('cnpj'))
    if erro:
        return erro 
    
    erro = valida_status(dados.get('status'))
    if erro:
        return erro 

    erro = valida_valor(dados.get('valor'))
    if erro:
        return erro  

    erro = valida_descricao(dados.get('descricao'))
    if erro:
        return erro 

    erro = valida_data_vencimento(dados.get('data_vencimento'))
    if erro:
        return erro 

    erro = valida_multa(dados.get('multa'))
    if erro:
        return erro 

    erro = valida_data_pagamento(dados.get('data_pagamento'))
    if erro:
        return erro  

    erro = valida_juros(dados.get('juros'))
    if erro:
        return erro  

    return None  


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
    if not (isinstance(telefone, (str)) and len (telefone) > 8 and telefone.isdigit()):
        return {"Mensagem": "Telefone inválido!"}
    return None

def valida_dados_credor(dados):
    erro = valida_cnpj(dados.get('cnpj'))
    if erro:
        return erro 
    
    erro = valida_nome(dados.get('nome'))
    if erro:
        return erro  
    
    erro = valida_endereco(dados.get('endereco'))
    if erro:
        return erro  
    
    erro = valida_telefone(dados.get('telefone'))
    if erro:
        return erro
    
    erro = valida_email(dados.get('email'))
    if erro:
        return erro 
    
    return None  



