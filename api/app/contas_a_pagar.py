from flask import jsonify, request,Blueprint
from .models import db,ContaAPagar,Credor 
from .utils.validacoes import valida_dados_contas_a_pagar,valida_data_pagamento,valida_valor



contas_bp = Blueprint('contas_bp', __name__)



@contas_bp.route('/listar', methods=['GET'])
def listar_contas():
    cnpj = request.args.get('cnpj')
    data_vencimento = request.args.get('data_vencimento')

    credores_query = Credor.query

  
    if cnpj:
        credores_query = credores_query.filter(Credor.cnpj == cnpj)  
    if data_vencimento:
        credores_query = credores_query.filter(ContaAPagar.data_vencimento == data_vencimento)    
    credores = credores_query.all()

    response = []
    for credor in credores:
        empresa = {'nome':credor.nome,'cnpj':credor.cnpj}
        contas = [{'id':conta.id,'valor': conta.valor, 'descricao': conta.descricao,'data_vencimento':conta.data_vencimento,'data_pagamento':conta.data_pagamento} for conta in credor.contas]
        if len(contas) > 0:
            response.append({'empresa': empresa, 'contas': contas})
    return response



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
            'credor': {
                'nome': conta.credor.nome,
                'cnpj':conta.cnpj,
            }
        }
        return  response, 201
    else:
       return jsonify({"mensagem": "Conta não encontrada"}), 400

@contas_bp.route('/adicionar' ,methods=['POST'])
def adicionar_conta():
    if not request.json or 'cnpj' not in request.json or 'data_vencimento' not in request.json or 'valor' not in request.json  or 'juros' not in request.json or  'descricao' not in request.json :
        return jsonify({"mensagem": "Preencha todos os campos"}), 400
    try:   
        dados = request.json  
        valida_dados_contas_a_pagar(dados)  
        credor = Credor.query.get(dados['cnpj'])
        if not credor:
            return jsonify({"mensagem": "Credor não cadastrado!"}), 400
        nova_conta = ContaAPagar(
            valor=dados['valor'],
            descricao=dados['descricao'],
            data_vencimento=dados['data_vencimento'],
            data_pagamento=dados.get('data_pagamento'),
            multa=dados.get('multa'),
            juros=dados.get('juros'),
            cnpj=dados['cnpj']
        )
        
        db.session.add(nova_conta)
        db.session.commit()

        return jsonify({"mensagem": "Conta adicionada com sucesso!"}), 201

    except KeyError as error:
        return jsonify({"mensagem": f"Campo obrigatório ausente: {error}"}), 400

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
                return jsonify({"mensagem": "Credor não cadastrado!"}), 400
        
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
            
        db.session.commit()    
            
        return jsonify({"mensagem": "Conta atualizada com sucesso!"}), 201

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
        if not data_pagamento:
            return jsonify({"erro": "Data de pagamento é obrigatória!"}), 400
        if not valor:
            return jsonify({"erro": "Valor é obrigatória!"}), 400
        
        valida_data_pagamento(data_pagamento)
        valida_valor(valor)
        conta.data_pagamento = data_pagamento
        conta.valor = valor
        db.session.commit()

        return jsonify({"mensagem": "Pagamento efetuado com sucesso!"}), 200

    except Exception as e:
        return jsonify({"erro": f"Erro ao pagar a conta: {str(e)}"}), 500       
        
    

@contas_bp.route('/remover/<int:id>', methods=['DELETE'])
def deletar_conta(id):
    conta = ContaAPagar.query.get(id)
    if conta:
        try:
            db.session.delete(conta)
            db.session.commit()
            return jsonify({"Mensagem": "Conta deletada com sucesso"}), 201
        except KeyError as error:
            return jsonify({"mensagem": f"Campo obrigatório ausente: {error}"}), 400
        except Exception as error:
            return jsonify({"erro": f"Erro ao deletar a conta: {str(error)}"}), 500     
    else:
       return jsonify({"mensagem": "Conta não encontrada"}), 400

    

