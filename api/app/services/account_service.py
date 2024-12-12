from ..database import db
from ..models.account_model import Accounts
from ..models.creditor_model import Creditors
from ..utils.validacoes import valida_dados_contas_a_pagar,valida_data_pagamento,valida_data_vencimento,valida_valor,valida_status
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


class AccountService:

    def get_all(due_date=None,payment_date=None,cnpj=None, status=None):
        try:
            query = Accounts.query 
            if due_date:
                due_date_date = datetime.strptime(due_date, '%Y-%m-%d').date()
                query = query.filter(Accounts.due_date == due_date_date)      
            if payment_date:
                payment_date_date = datetime.strptime(payment_date, '%Y-%m-%d').date()
                query = query.filter(Accounts.payment_date == payment_date_date)      
            if cnpj:
                query = query.filter(Accounts.cnpj == cnpj)     
            if status:
                query = query.filter(Accounts.status == status)   
            accounts = query.all()   
            response = {
                'value': [
                    {
                        'cnpj': account.cnpj,
                        'id': account.id,
                        'amount': account.amount,
                        'description': account.description,
                        'due_date': account.due_date,
                        'status': account.status,
                        'payment_date': account.payment_date
                    }
                    for account in accounts
                ],
                'message': None,
                'statusCode': 200
}
            
            return response  
        except Exception as e:
                    raise Exception({'value':None,'message':f"Erro ao listar contas: {str(e)}",'statusCode':500})

    def get_by_id(id):
        account = Accounts.query.get(id)
        if account:
            response = {
                'id': account.id,
                'amount': float(account.amount) if account.amount else 0.0,
                'description': account.description,
                'due_date': account.due_date,
                'payment_date': account.payment_date,
                'penalty': float(account.penalty) if account.penalty else 0.0,
                'interest': float(account.interest) if account.interest else 0.0,
                'status': account.status,
                'creditor': {
                    'name': account.creditor.name,
                    'cnpj': account.cnpj,
                }
            }

            return {'value': response, 'message':None, 'statusCode':200}
        else:
            return {'value':None,'message': 'Conta não encontrada', 'statusCode':400}
    
    


    def register(data):
        if not data:
            return {'value': None, 'message': 'Preencha todos os campos', 'statusCode': 400}

        try:
            error = valida_dados_contas_a_pagar(data)
            if error:
                return {'value': None, 'message': error, 'statusCode': 400}

            creditor = Creditors.query.get(data['cnpj'])
            if not creditor:
                return {'value': None, 'message': 'Credor não cadastrado!', 'statusCode': 400}

            new_account = Accounts(
            amount=data['amount'],
            description=data['description'],
            due_date=datetime.strptime(data['due_date'], '%Y-%m-%d').date(),
            payment_date=(datetime.strptime(data['payment_date'], '%Y-%m-%d').date()
                        if 'payment_date' in data and data['payment_date'] else None),
            penalty=data.get('penalty'),
            interest=data.get('interest'),
            cnpj=data['cnpj'],
            status=data['status']
        )


            db.session.add(new_account)
            db.session.commit()

            return {'value': 'Conta adicionada com sucesso!', 'message':None , 'statusCode': 201}

        except KeyError as error:
            return {'value': None, 'message': f"Campo obrigatório ausente: {error}", 'statusCode': 400}

        except SQLAlchemyError as error:
            db.session.rollback()
            return {'value': None, 'message': f"Erro ao salvar a conta no banco: {str(error)}", 'statusCode': 500}

        except Exception as error:
            return {'value': None, 'message': f"Erro inesperado: {str(error)}", 'statusCode': 500}

        
        
        

    def update(id, data):
        account = Accounts.query.get(id)
        if not account:
            return {'value': None, 'message': "Conta não encontrada!", 'statusCode': 404}

        try:
            valida_dados_contas_a_pagar(data)

            if 'cnpj' in data:
                credor = Creditors.query.get(data['cnpj'])
                if not credor:
                    return {'value': None, 'message': "Credor não cadastrado!", 'statusCode': 400}

            data.amount = data.get('amount', data.amount)
            data.description = data.get('description', data.description)
            data.due_date = data.get('due_date', data.due_date)
            data.payment_date = data.get('payment_date', data.payment_date)
            data.penalty = data.get('penalty', data.penalty)
            data.interest = data.get('interest', data.interest)
            data.cnpj = data.get('cnpj', data.cnpj)
            data.status = data.get('status', data.status)


            db.session.commit()
            return {'value': 'Conta atualizada com sucesso!', 'message': None, 'statusCode': 200}

        except SQLAlchemyError as e:
            db.session.rollback()
            return {'value': None, 'message': f"Erro ao atualizar a conta: {str(e)}", 'statusCode': 500}
        
        

    def pay(id, data):
        account = Accounts.query.get(id)
        if not account:
            return {'value': None, 'message': "Conta não encontrada!", 'statusCode': 404}

        try:
            payment_date = data.get('payment_date')
            amount = data.get('amount')
            status = data.get('status')

            if not status:
                return {'value': None, 'message': "Status is required!", 'statusCode': 400}
            if not payment_date:
                return {'value': None, 'message': "Payment date is required!", 'statusCode': 400}
            if not amount:
                return {'value': None, 'message': "Amount is required!", 'statusCode': 400}

            error_payment = valida_data_pagamento(payment_date)
            if error_payment:
                return {'value': None, 'message': error_payment, 'statusCode': 400}

            error_amount = valida_valor(amount)
            if error_amount:
                return {'value': None, 'message': error_amount, 'statusCode': 400}

            error_status = valida_status(status)
            if error_status:
                return {'value': None, 'message': error_status, 'statusCode': 400}

            account.payment_date = payment_date
            account.amount = amount
            account.status = status
            db.session.commit()

            return {'value':  "Pagamento efetuado com sucesso!", 'message':None, 'statusCode': 200}

        except SQLAlchemyError as e:
            db.session.rollback()
            return {'value': None, 'message': f"Erro ao pagar a conta: {str(e)}", 'statusCode': 500}

            
        

    def update_status(id, dados):
        account = Accounts.query.get(id)
        if not account:
            return {'value': None, 'message': "Conta não encontrada!", 'statusCode': 404}

        try:
            status = dados.get('status')
            if not status:
                return {'value': None, 'message': "Status é obrigatório!", 'statusCode': 400}

            valida_status(status)
            account.status = status
            db.session.commit()

            return {'value': "Atualização efetuada com sucesso!", 'message': None, 'statusCode': 200}

        except SQLAlchemyError as e:
            db.session.rollback()
            return {'value': None, 'message': f"Erro ao atualizar a conta: {str(e)}", 'statusCode': 500}
            

    def delete(id):
        account = Accounts.query.get(id)
        if account:
            try:
                db.session.delete(account)
                db.session.commit()
                return {'value': 'Conta deletada com sucesso','message':None, 'statusCode': 201}
            except KeyError as error:
                return {'value':None,'message': f"Campo obrigatório ausente: {error}", 'statusCode':500}
            except Exception as error:
                return {'value':None,'message': f"Erro ao deletar a conta: {str(error)}", 'statusCode':500}     
        else:
            return {'value':None,'message': 'Conta não encontrada', 'statusCode': 400}, 
