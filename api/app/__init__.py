from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .database import db

# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    CORS(app)

    from .routes.account_route import account_bp
    from .routes.creditor_route import credores_bp

    #app.register_blueprint(credor_bp, url_prefix='/credores')
    app.register_blueprint(account_bp, url_prefix='/accounts')
    app.register_blueprint(credores_bp,url_prefix='/creditors')

    with app.app_context():
        db.create_all()

    return app
