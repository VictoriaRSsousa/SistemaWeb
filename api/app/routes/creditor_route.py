from flask import Blueprint

from ..controllers.creditor_controller import CredorController
credores_bp = Blueprint('credores_bp', __name__)


credores_bp.route('/', methods=['GET'])(CredorController.get_all)
credores_bp.route('/<string:cnpj>', methods=['GET'])(CredorController.get_by_cnpj)
credores_bp.route('/create', methods=['POST'])(CredorController.register)
credores_bp.route('/update/<string:cnpj>', methods=['PUT'])(CredorController.update)
credores_bp.route('/delete/<string:cnpj>', methods=['DELETE'])(CredorController.delete)

