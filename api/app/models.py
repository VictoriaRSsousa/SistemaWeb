from . import db

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

