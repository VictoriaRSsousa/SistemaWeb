from flask import jsonify, request,Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from utils.validacoes import valida_dados_credor

#inicialização
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/contas_a_pagar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
CORS(app) 

#MODEL
class Credor(db.Model):
    __tablename__ = 'credores'
    cnpj = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))

#rotas
@app.route('/listarCredores', methods=['GET'])
def listar_credores():
    try:
        credores = Credor.query.all()
        return jsonify([{
            'cnpj': credor.cnpj,
            'nome': credor.nome,
            'endereco': credor.endereco,
            'telefone': credor.telefone,
            'email': credor.email


        }for credor in credores]), 200
    except Exception as e:
        return jsonify({'error': str(e)}),500
    

@app.route('/adicionarCredor', methods=['POST'])
def adicionar_credor():
    data = request.json
    
    if not request.json or 'cnpj' not in request.json or 'nome' not in request.json or 'endereco' not in request.json  or 'telefone' not in request.json or  'email' not in request.json :
        return jsonify({"mensagem": "Preencha todos os campos"}), 400
    
    erros = valida_dados_credor(data)
    try: 
        credor = Credor.query.get(data['cnpj'])
        if  credor:
            return jsonify({"mensagem": "Credor já cadastrado!"}), 400
        novo_credor = Credor(
            cnpj=data['cnpj'],
            nome=data['nome'],
            endereco=data['endereco'],
            telefone=data.get('telefone'),
            email=data.get('email')
        )
        db.session.add(novo_credor)
        db.session.commit()
        return jsonify({'message': 'Credor adicionado com sucesso!'}), 201
        
    except KeyError as error:
        return jsonify({"mensagem": f"Campo obrigatório ausente: {error}"}), 400

    except Exception as error:
        return jsonify({"erro": f"Erro ao adicionar a Credor: {str(error)}"}), 500

        

    
@app.route('/atualizarCredor/<int:cnpj>', methods=['PATCH'])
def atualizar_credor(cnpj):
    credor = Credor.query.get(cnpj)
    if not credor:
        return jsonify({"Mensagem": "Credor não encontrado!"}), 404   
    dados = request.json
    try:       
        if 'cnpj' not in dados and 'nome' not in dados and 'endereco' not in dados and 'telefone' not in dados and 'email' not in dados: 
            return jsonify({"mensagem":"Campo incorreto!"}),400   
        if 'cnpj' in dados:
            credor.cnpj = dados['cnpj']
        if 'nome' in dados:
            credor.nome = dados['nome']
        if 'endereco' in dados:
            credor.endereco = dados['endereco']
        if 'telefone' in dados:
            credor.telefone = dados['telefone']
        if 'email' in dados:
            credor.email = dados['email']
            
        db.session.commit()
        return jsonify({"mensagem": "Credor atualizado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"erro": f"Erro ao atualizar o credor: {str(e)}"}), 500
    



@app.route('/deletarCredor/<string:cnpj>', methods=['DELETE'])
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
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)   




