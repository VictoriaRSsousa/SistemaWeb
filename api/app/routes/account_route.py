from flask import Blueprint
from ..controllers.account_controller import AccountController

account_bp = Blueprint('account_bp', __name__)


account_bp.route('/', methods=['GET'])(AccountController.get_all)
account_bp.route('/<int:id>', methods=['GET'])(AccountController.get_by_id)
account_bp.route('/create', methods=['POST'])(AccountController.register)
account_bp.route('/update/<int:id>', methods=['PUT'])(AccountController.update)
account_bp.route('/delete/<int:id>', methods=['DELETE'])(AccountController.delete)
account_bp.route('/pay/<int:id>', methods=['PATCH'])(AccountController.pay)
account_bp.route('/updateStatus/<int:id>', methods=['PATCH'])(AccountController.update_status)
