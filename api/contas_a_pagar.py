from flask import jsonify, request,Blueprint, Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from utils.validacoes import valida_dados_contas_a_pagar
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/contas_a_pagar'
db = SQLAlchemy(app)
CORS(app) 
class Credor(db.Model):
    __tablename__ = 'credores'
    cnpj = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    
class ContaAPagar(db.Model):
    __tablename__ = 'contas_a_pagar'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.String(14), db.ForeignKey('credores.cnpj'), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    descricao = db.Column(db.String(255))
    data_vencimento = db.Column(db.Date, nullable=False)
    multa = db.Column(db.Numeric(10, 2))
    data_pagamento = db.Column(db.Date)
    juros = db.Column(db.Numeric(10, 2))

    credor = db.relationship('Credor', backref='contas')    

@app.route('/listarConta', methods=['GET'])
def listar_contas():
    cnpj = request.args.get('cnpj')
    data_vencimento = request.args.get('data_vencimento')

    credores_query = Credor.query

  
    if cnpj:
        credores_query = credores_query.filter(Credor.cnpj == cnpj)

    credores = credores_query.all()

    response = []
    for credor in credores:
        empresa = {'nome':credor.nome,'cnpj':credor.cnpj}
        contas = [{'id':conta.id,'valor': conta.valor, 'descricao': conta.descricao,'data_vencimento':conta.data_vencimento,'data_pagamento':conta.data_pagamento} for conta in credor.contas]
        if len(contas) > 0:
            response.append({'empresa': empresa, 'contas': contas})
    return response



@app.route('/conta/<int:id>', methods=['GET'])
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
        return jsonify({"Conta": response}), 201
    else:
       return jsonify({"mensagem": "Conta não encontrada"}), 400

@app.route('/adicionarConta' ,methods=['POST'])
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
    
    
    
@app.route('/atualizarConta/<int:id>' ,methods=['PATCH'])
def atualizar_conta(id):
    conta = ContaAPagar.query.get(id)
    if not conta:
        return jsonify({"Mensagem": "Conta não encontrada!"}), 404 
    dados = request.json
    try:       
        if 'valor' not in dados and 'cnpj' not in dados and 'juros' not in dados and 'multa' not in dados and 'data_pagamento' not in dados and 'data_vencimento' not in dados and 'descricao' not in dados: 
            return jsonify({"mensagem":"Campo incorreto!"}),400   
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
        
    

@app.route('/removerConta/<int:id>', methods=['DELETE'])
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


@app.route('/teste', methods=['POST'])
def valida_texto():
    cnpj = request.json['cnpj']
    credor = Credor.query.get(cnpj)
    if credor:
        return jsonify("tem")
    else:
        return jsonify("nao tem")
   # return {"retorno":credor}
    
if __name__ == '__main__':
    # Certifique-se de que o SQLAlchemy está inicializado antes de criar as tabelas
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
#TODO - implement validation functions on create and update

