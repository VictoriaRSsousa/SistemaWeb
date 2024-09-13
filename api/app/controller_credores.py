from flask import jsonify, request,Blueprint

from flask import jsonify, request,Blueprint
from .models import db,Credor 
from .utils.validacoes import valida_cnpj



from utils.validacoes import valida_dados_credor

credores_bp = Blueprint('credores_bp', __name__)


#rotas
@credores_bp.route('/', methods=['GET'])
def listar_credores():
    try:
        cnpj = request.args.get('cnpj')
        credores_query = Credor.query
        if cnpj:
            valida_cnpj(cnpj)
            credores_query = credores_query.filter(Credor.cnpj == cnpj)  
        credores = credores_query.all()
        return jsonify([{
            'cnpj': credor.cnpj,
            'nome': credor.nome,
            'endereco': credor.endereco,
            'telefone': credor.telefone,
            'email': credor.email


        }for credor in credores]), 200
    except Exception as e:
        return jsonify({'error': str(e)}),500
    

@credores_bp.route('/<int:cnpj>', methods=['GET'])
def selecionar_credor_por_id(cnpj):
    credor = Credor.query.get(cnpj)
    if credor:
        response = {
            'cnpj':credor.cnpj,
            'nome': credor.nome,
            'endereco': credor.endereco,
            'telefone': credor.telefone,
            'email':credor.email,
        
            
        }
        return  response, 201
    else:
       return jsonify({"mensagem": "Credor não encontrado"}), 400
    

@credores_bp.route('/adicionar', methods=['POST'])
def adicionar_credor():
    dados = request.json
    
    if not request.json or 'cnpj' not in request.json or 'nome' not in request.json or 'endereco' not in request.json  or 'telefone' not in request.json or  'email' not in request.json :
        return jsonify({"mensagem": "Preencha todos os campos"}), 400
    
    valida_dados_credor(dados)
    try: 
        credor = Credor.query.get(dados['cnpj'])
        if  credor:
            return jsonify({"mensagem": "Credor já cadastrado!"}), 400
        novo_credor = Credor(
            cnpj=dados['cnpj'],
            nome=dados['nome'],
            endereco=dados['endereco'],
            telefone=dados.get('telefone'),
            email=dados.get('email')
        )
        db.session.add(novo_credor)
        db.session.commit()
        return jsonify({'message': 'Credor adicionado com sucesso!'}), 201
        
    except KeyError as error:
        return jsonify({"mensagem": f"Campo obrigatório ausente: {error}"}), 400

    except Exception as error:
        return jsonify({"erro": f"Erro ao adicionar a Credor: {str(error)}"}), 500

        

    
@credores_bp.route('/atualizar/<int:cnpj>', methods=['PUT'])
def atualizar_credor(cnpj):
    credor = Credor.query.get(cnpj)
    if not credor:
        return jsonify({"Mensagem": "Credor não encontrado!"}), 404  
    dados = request.json

    valida_dados_credor(dados)
    #NAO TA VALIDANDO CORRETAMENTE 
    try:       
        credor.nome = dados.get('nome', credor.nome)
        credor.endereco = dados.get('endereco', credor.endereco)
        credor.telefone = dados.get('telefone', credor.telefone)
        credor.email = dados.get('email', credor.email)
        credor.cnpj = dados.get('cnpj', credor.cnpj)
            
        db.session.commit()
        return jsonify({"mensagem": "Credor atualizado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"erro": f"Erro ao atualizar o credor: {str(e)}"}), 500
    



@credores_bp.route('/deletar/<string:cnpj>', methods=['DELETE'])
def deletar_credor(cnpj):
    try:
        credor = Credor.query.get(cnpj)
        if not credor:
            return jsonify({'error': 'Credor não encontrado'}), 404
        
        db.session.delete(credor)
        db.session.commit()
        return jsonify({"message": "Credor deletador com sucesso!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    



