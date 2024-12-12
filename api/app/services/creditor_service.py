from ..database import db
from sqlalchemy.exc import SQLAlchemyError
from ..models.creditor_model import Creditors
from ..utils.validacoes import *

class CredorService:
    def get_all(cnpj=None):
        try:
            query = Creditors.query
            if cnpj:
                query = query.filter(Creditors.cnpj == cnpj)
            creditors = query.all()    
            return {
        'value': [{
            'cnpj': creditor.cnpj,
            'name': creditor.name,
            'address': creditor.address,
            'phone': creditor.phone,
            'email': creditor.email
        } for creditor in creditors],
        'message': None,
        'statusCode': 200
    }
        except Exception as e:
            raise Exception({'value':None,'message':f"Erro ao listar credores: {str(e)}",'statusCode':500})

    def get_by_cnpj(cnpj):
        try:
            creditor = Creditors.query.get(cnpj)
            if not creditor:
                return {
                    'value': None,
                    'message': 'Credor não encontrado',
                    'statusCode': 404
                }
            return {
                'value': {
                    'cnpj': creditor.cnpj,
                    'name': creditor.name,
                    'address': creditor.address,
                    'phone': creditor.phone,
                    'email': creditor.email
                },
                'message': None,
                'statusCode': 200
            }
        except Exception as e:
            return {
            'value': None,
            'message': str(e),
            'statusCode': 500
        }
    
    def register(data):
        if not data:
             return{'value': None,'message':'Dados inválidos.', 'statusCode':400}
        error = valida_dados_credor(data)
        if(error):
            return{'value': None,'message':jsonify(error), 'statusCode':400}
        try:
            new_creditor = Creditors(
                cnpj=data['cnpj'],
                name=data['name'],
                address=data['address'],
                phone=data['phone'],
                email=data['email']
            )
            db.session.add(new_creditor)
            db.session.commit()
            return {'value':'Cadastro realizado com sucesso!','message': None, 'statusCode':200}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {
                'value': None,
                'message': f"Erro ao adicionar credor: {str(e)}",
                'statusCode': 500
            }
        except Exception as e:
            return {
                'value': None,
                'message': f"Erro inesperado: {str(e)}",
                'statusCode': 500
            }

    def update(cnpj, data):
        if not data:
            return{'value': None,'message':'Dados inválidos.', 'statusCode':400}
        error = valida_dados_credor(data)
        if(error):
            return{'value': None,'message':jsonify(error), 'statusCode':400}
        creditor = Creditors.query.get(cnpj)
        if not creditor:
            return {
                'value': None,
                'message': "Credor não encontrado",
                'statusCode': 404
            }

        try:
            creditor.name = data.get('name', creditor.name)
            creditor.address = data.get('address', creditor.address)
            creditor.phone = data.get('phone', creditor.phone)
            creditor.email = data.get('email', creditor.email)
            db.session.commit()

            return {
                'value': 'Credor atualizado com sucesso!',
                'message': None,
                'statusCode': 200
            }

        except SQLAlchemyError as e:
            db.session.rollback()
            return {
                'value': None,
                'message': f"Erro ao atualizar credor: {str(e)}",
                'statusCode': 500
            }

        except Exception as e:
            return {
                'value': None,
                'message': f"Erro inesperado: {str(e)}",
                'statusCode': 500
            }

    def delete(cnpj):
        creditor = Creditors.query.get(cnpj)
        if not creditor:
            return {
                'value': None,
                'message': "Credor não encontrado",
                'statusCode': 404
            }

        try:
            db.session.delete(creditor)
            db.session.commit()

            return {
                'value': "Credor deletado",
                'message':None ,
                'statusCode': 200
            }

        except SQLAlchemyError as e:
            db.session.rollback()
            return {
                'value': None,
                'message': f"Erro ao deletar credor: {str(e)}",
                'statusCode': 500
            }

        except Exception as e:
            return {
                'value': None,
                'message': f"Erro inesperado: {str(e)}",
                'statusCode': 500
            }
