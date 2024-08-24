from flask import  jsonify
from datetime import datetime 

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
    erros = []

    erro = valida_cnpj(dados.get('cnpj'))
    if erro: erros.append(erro)

    erro = valida_valor(dados.get('valor'))
    if erro: erros.append(erro)

    erro = valida_descricao(dados.get('descricao'))
    if erro: erros.append(erro)

    erro = valida_data_vencimento(dados.get('data_vencimento'))
    if erro: erros.append(erro)

    erro = valida_multa(dados.get('multa'))
    if erro: erros.append(erro)

    erro = valida_data_pagamento(dados.get('data_pagamento'))
    if erro: erros.append(erro)

    erro = valida_juros(dados.get('juros'))
    if erro: erros.append(erro)

    if erros:
        return jsonify({"Erros": erros})

    return jsonify({"Mensagem": "Dados válidos!"})