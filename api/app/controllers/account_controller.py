from flask import jsonify, request
from ..services.account_service import AccountService


class AccountController:
    
    def get_all():
        due_date = request.args.get('data_vencimento')
        payment_date = request.args.get('data_pagamento')
        cnpj = request.args.get('cnpj')
        status = request.args.get('status') 
        accounts =  AccountService.get_all(due_date,payment_date,cnpj,status)
        if(accounts['message']):
            return jsonify(accounts['message']), accounts['statusCode']
        else:
            return jsonify(accounts['value']), accounts['statusCode']  


    def get_by_id(id):
        account = AccountService.get_by_id(id)
        if(account['message']):
            return jsonify(account['message']), account['statusCode']
        else:
            return jsonify(account['value']), account['statusCode']  
    
    
    

    def register():
        data = request.json   
        account = AccountService.register(data)
        if(account['message']):
            return jsonify(account['message']), account['statusCode']
        else:
            return jsonify(account['value']), account['statusCode']  
    
        
        
        
    def update(id):
        data = request.json
        account = AccountService.update(id,account)
        if(account['message']):
            return jsonify(account['message']), account['statusCode']
        else:
            return jsonify(account['value']), account['statusCode']  
        
        
  
    def pay(id):
        data = request.json
        account = AccountService.pay(id,data)
        if(account['message']):
            return jsonify(account['message']), account['statusCode']
        else:
            return jsonify(account['value']), account['statusCode']  
    
            

    def update_status(id):
        data = request.json
        status = data.get('status')     
        account = AccountService.update_status(id,status)
        if(account['message']):
            return jsonify(account['message']), account['statusCode']
        else:
            return jsonify(account['value']), account['statusCode']  
            

    def delete(id):
        account = AccountService.delete(id)
        if(account['message']):
            return jsonify(account['message']), account['statusCode']
        else:
            return jsonify(account['value']), account['statusCode']  
    

    