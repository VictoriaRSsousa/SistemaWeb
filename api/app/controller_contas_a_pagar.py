from flask import jsonify, request,Blueprint
from .models import db,ContaAPagar,Credor 
from .utils.validacoes import valida_dados_contas_a_pagar,valida_data_pagamento,valida_data_vencimento,valida_valor,valida_status
from datetime import datetime, date



contas_bp = Blueprint('contas_bp', __name__)



@contas_bp.route('/', methods=['GET'])
def listar_contas():
    data_vencimento = request.args.get('data_vencimento')
    data_pagamento = request.args.get('data_pagamento')
    cnpj = request.args.get('cnpj')
    status = request.args.get('status')  # Novo filtro de status
    
    contas_query = ContaAPagar.query 
    if data_vencimento:
        data_vencimento_date = datetime.strptime(data_vencimento, '%Y-%m-%d').date()
        contas_query = contas_query.filter(ContaAPagar.data_vencimento == data_vencimento_date)      
    if data_pagamento:
        data_pagamento_date = datetime.strptime(data_pagamento, '%Y-%m-%d').date()
        contas_query = contas_query.filter(ContaAPagar.data_pagamento == data_pagamento_date)      
    if cnpj:
        contas_query = contas_query.filter(ContaAPagar.cnpj == cnpj)     
    if status:
        contas_query = contas_query.filter(ContaAPagar.status == status)  # Filtra pelo status   
    contas = contas_query.all()   
    response = [
        {
            'cnpj': conta.cnpj,
            'id': conta.id,
            'valor': conta.valor,
            'descricao': conta.descricao,
            'data_vencimento': conta.data_vencimento,
            'status': conta.status,
            'data_pagamento': conta.data_pagamento
        }
        for conta in contas
    ]
    
    return jsonify(response)  



@contas_bp.route('/<int:id>', methods=['GET'])
def selecionar_conta_por_id(id):
    conta = ContaAPagar.query.get(id)
    if conta:
        response = {
            'id':conta.id,
            'valor': conta.valor,
            'descricao': conta.descricao,
            'data_vencimento': conta.data_vencimento,
            'data_pagamento':conta.data_pagamento,
            'multa':conta.multa,
            'juros':conta.juros,
            'status':conta.status,
            'credor': {
                'nome': conta.credor.nome,
                'cnpj':conta.cnpj,
            }
        }
        return response, 201
    else:
       return jsonify({"Mensagem": "Conta não encontrada"}), 400

@contas_bp.route('/adicionar', methods=['POST'])
def adicionar_conta():
    if not request.json or 'cnpj' not in request.json or 'data_vencimento' not in request.json or 'valor' not in request.json or 'juros' not in request.json or 'descricao' not in request.json:
        return jsonify({"Mensagem": "Preencha todos os campos"}), 400
    
    try:
        dados = request.json
        erro = valida_dados_contas_a_pagar(dados)  
        if erro:
            return jsonify(erro), 400 
        
        credor = Credor.query.get(dados['cnpj'])
        if not credor:
            return jsonify({"Mensagem": "Credor não cadastrado!"}), 400
        
        nova_conta = ContaAPagar(
            valor=dados['valor'],
            descricao=dados['descricao'],
            data_vencimento=dados['data_vencimento'],
            data_pagamento=dados.get('data_pagamento'),
            multa=dados.get('multa'),
            juros=dados.get('juros'),
            cnpj=dados['cnpj'],
            status = dados['status']
        )
        
        db.session.add(nova_conta)
        db.session.commit()

        return jsonify({"Mensagem": "Conta adicionada com sucesso!"}), 201

    except KeyError as error:
        return jsonify({"Mensagem": f"Campo obrigatório ausente: {error}"}), 400

    except Exception as error:
        return jsonify({"erro": f"Erro ao adicionar a conta: {str(error)}"}), 500

    
    
    
@contas_bp.route('/atualizar/<int:id>' ,methods=['PUT'])
def atualizar_conta(id):
    conta = ContaAPagar.query.get(id)
    if not conta:
        return jsonify({"Mensagem": "Conta não encontrada!"}), 404 
    dados = request.json
    try:       
       
        valida_dados_contas_a_pagar(dados)  
        if 'cnpj' in dados:
            credor = Credor.query.get(dados['cnpj'])
            if not credor:
                return jsonify({"Mensagem": "Credor não cadastrado!"}), 400
        
        if 'valor' in dados:
            conta.valor = dados['valor']
        if 'descricao' in dados:
            conta.descricao = dados['descricao']
        if 'data_vencimento' in dados:
            conta.data_vencimento = dados['data_vencimento']
        if 'data_pagamento' in dados:
            conta.data_pagamento = dados['data_pagamento']
        if 'multa' in dados:
            conta.multa = dados['multa']
        if 'juros' in dados:
            conta.juros = dados['juros']
        if 'cnpj' in dados:
            conta.cnpj = dados['cnpj']
        conta.status = dados['status']    
            
        db.session.commit()    
            
        return jsonify({"Mensagem": "Conta atualizada com sucesso!"}), 201

    except Exception as e:
        return jsonify({"erro": f"Erro ao atualizar a conta: {str(e)}"}), 500 
    
    
@contas_bp.route('/pagar/<int:id>' ,methods=['PATCH'])  
def pagar_conta(id):
    conta = ContaAPagar.query.get(id)
    if not conta:
        return jsonify({"Mensagem": "Conta não encontrada!"}), 404

    dados = request.json
    try:
        data_pagamento = dados.get('data_pagamento')
        valor = dados.get('valor')
        status = dados.get('status')
        if not status:
            return jsonify({"erro": "Status  é obrigatório!"}), 400
        if not data_pagamento:
            return jsonify({"erro": "Data de pagamento é obrigatória!"}), 400
        if not valor:
            return jsonify({"erro": "Valor é obrigatória!"}), 400
        
        valida_data_pagamento(data_pagamento)
        valida_valor(valor)
        valida_status(status)
        conta.data_pagamento = data_pagamento
        conta.valor = valor
        conta.status = status
        db.session.commit()

        return jsonify({"Mensagem": "Pagamento efetuado com sucesso!"}), 200

    except Exception as e:
        return jsonify({"erro": f"Erro ao pagar a conta: {str(e)}"}), 500       
        
    
@contas_bp.route('/atualizarStatus/<int:id>' ,methods=['PATCH'])  
def atualizarStatus(id):
    conta = ContaAPagar.query.get(id)
    if not conta:
        return jsonify({"Mensagem": "Conta não encontrada!"}), 404

    dados = request.json
    try:
        status = dados.get('status')
        if not status:
            return jsonify({"erro": "Status  é obrigatório!"}), 400
        valida_status(status)
        conta.status = status
        db.session.commit()

        return jsonify({"Mensagem": "Atualização efetuada com sucesso!"}), 200

    except Exception as e:
        return jsonify({"erro": f"Erro ao atualizar a conta: {str(e)}"}), 500   
        
@contas_bp.route('/remover/<int:id>', methods=['DELETE'])
def deletar_conta(id):
    conta = ContaAPagar.query.get(id)
    if conta:
        try:
            db.session.delete(conta)
            db.session.commit()
            return jsonify({"Mensagem": "Conta deletada com sucesso"}), 201
        except KeyError as error:
            return jsonify({"Mensagem": f"Campo obrigatório ausente: {error}"}), 400
        except Exception as error:
            return jsonify({"erro": f"Erro ao deletar a conta: {str(error)}"}), 500     
    else:
       return jsonify({"Mensagem": "Conta não encontrada"}), 400

    

# @contas_bp.route('/atualizar-contas-atrasadas', methods=['GET'])
# def atualizar_contas_atrasadas():
#     try:
#         # Obter a data atual
#         data_atual = date.today()
        
#         # Buscar todas as contas que estão vencidas e ainda não estão marcadas como "ATRASADA"
#         contas_vencidas = ContaAPagar.query.filter(
#             ContaAPagar.data_vencimento < data_atual,
#             ContaAPagar.status != 'ATRASADA',
#             ContaAPagar.data_pagamento.is_(None)  # Apenas contas não pagas
#         ).all()
        
#         # Atualizar o status dessas contas para "ATRASADA"
#         for conta in contas_vencidas:
#             conta.status = 'ATRASADA'
        
#         # Salvar as mudanças no banco de dados
#         db.session.commit()
        
#         return jsonify({"Mensagem": f"{len(contas_vencidas)} contas atualizadas como ATRASADA!"}), 200
    
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"erro": f"Erro ao atualizar contas: {str(e)}"}), 500
