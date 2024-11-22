from flask import jsonify, request,Blueprint
from .models import db,Credor 
from .utils.validacoes import valida_cnpj,valida_dados_credor
from sqlalchemy.exc import SQLAlchemyError
import traceback

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
       return jsonify({"Mensagem": "Credor nao encontrado"}), 400
    

@credores_bp.route('/create', methods=['POST'])
def adicionar_credor():
    if not request.json:
        return jsonify({"Mensagem": "Dados inválidos"}), 400

    try:
        dados = request.json
        erro = valida_dados_credor(dados)
        if erro:
            return jsonify(erro), 400  
        
        novo_credor = Credor(
            cnpj=dados['cnpj'],
            nome=dados['nome'],
            endereco=dados['endereco'],
            telefone=dados['telefone'],
            email=dados['email']
        )
        
        db.session.add(novo_credor)
        db.session.commit()

        return jsonify({"Mensagem": "Credor adicionado com sucesso!"}), 201

    except Exception as error:
        return jsonify({"erro": f"Erro ao adicionar o credor: {str(error)}"}), 500

        

    
@credores_bp.route('/update/<string:cnpj>', methods=['PUT'])
def atualizar_credor(cnpj):
    credor = Credor.query.get(cnpj)
    if not credor:
        return jsonify({"Mensagem": "Credor não encontrado!"}), 404

    dados = request.json

    try:
        erro = valida_dados_credor(dados)
        if erro:
            return jsonify(erro), 400

        credor.nome = dados.get('nome', credor.nome)
        credor.endereco = dados.get('endereco', credor.endereco)
        credor.telefone = dados.get('telefone', credor.telefone)
        credor.email = dados.get('email', credor.email)
        credor.cnpj = dados.get('cnpj', credor.cnpj)
            
        db.session.commit()
        return jsonify({"Mensagem": "Credor atualizado com sucesso!"}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"erro": f"Erro ao atualizar o credor: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado: {str(e)}"}), 500



@credores_bp.route('/delete/<string:cnpj>', methods=['DELETE'])
def deletar_credor(cnpj):
    try:
        credor = Credor.query.get(cnpj)
        if not credor:
            return jsonify({'error': 'Credor nao encontrado'}), 404
        
        db.session.delete(credor)
        db.session.commit()
        return jsonify({"Mensagem": "Credor deletador com sucesso!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    



