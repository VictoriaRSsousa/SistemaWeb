from flask import Flask, jsonify, request, abort 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/contas_a_pagar'
db = SQLAlchemy(app)

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

@app.route('/contas' ,methods=['GET'])
def listar_contas():
    credores = Credor.query.all()
    response = []
    for credor in credores:
        empresa = [{'nome':credor.nome,'cnpj':credor.cnpj}]
        contas = [{'id':conta.id,'valor': conta.valor, 'descricao': conta.descricao,'data de vencimento':conta.data_vencimento,'data de pagamento':conta.data_pagamento} for conta in credor.contas]
        if len(contas) > 0:
            response.append({'empresa': empresa, 'contas': contas})
    return {'credores': response}



@app.route('/conta/<int:id>', methods=['GET'])
def pegar_conta_por_id(id):
    conta = ContaAPagar.query.get(id)
    if conta:
        response = {
            'id':conta.id,
            'valor': conta.valor,
            'descricao': conta.descricao,
            'data de vencimento': conta.data_vencimento,
            'data de pagamento':conta.data_pagamento,
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

@app.route('/adicionar_conta' ,methods=['POST'])
def adicionar_conta():
    try:
        dados = request.json
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
    
    
    
@app.route('/atualizar_conta/<int:id>' ,methods=['PATCH'])
def atualizar_conta(id):
    conta = ContaAPagar.query.get(id)
    if not conta:
        return jsonify({"Mensagem": "Conta não encontrada!"}), 404 
    dados = request.json
    try:       
        if 'valor' not in dados and 'cnpj' not in dados and 'juros' not in dados and 'multa' not in dados and 'data_pagamento' not in dados and 'data_vencimento' not in dados and 'descricao' not in dados: 
            return jsonify({"mensagem":"Campo incorreto!"})   
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
        
    

@app.route('/conta/<int:id>', methods=['DELETE'])
def deletar_conta_por_id(id):
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

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Creates the tables in the database
app.run(debug=True)



#TODO - implement validation functions on create and update