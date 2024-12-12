from flask import jsonify, request
from ..services.creditor_service import CredorService

class CredorController:
    def get_all():
        cnpj = request.args.get('cnpj')
        creditors = CredorService.get_all(cnpj)
        if(creditors['message']):
            return jsonify(creditors['message']), creditors['statusCode']
        else:
            return jsonify(creditors['value']), creditors['statusCode'] 

    def get_by_cnpj(cnpj):
            creditor = CredorService.get_by_cnpj(cnpj)
            if(creditor['message']):
                return jsonify(creditor['message']), creditor['statusCode']
            else:
                return jsonify(creditor['value']), creditor['statusCode'] 

    def register():
            data = request.json
            creditor = CredorService.register(data)
            if(creditor['message']):
                return jsonify(creditor['message']), creditor['statusCode']
            else:
                return jsonify(creditor['value']), creditor['statusCode'] 
           

    def update(cnpj):
        data = request.json
        creditor = CredorService.update(cnpj, data)
        if(creditor['message']):
            return jsonify(creditor['message']), creditor['statusCode']
        else:
            return jsonify(creditor['value']), creditor['statusCode'] 

    def delete(cnpj):
        creditor = CredorService.delete(cnpj)
        if(creditor['message']):
            return jsonify(creditor['message']), creditor['statusCode']
        else:
            return jsonify(creditor['value']), creditor['statusCode'] 
