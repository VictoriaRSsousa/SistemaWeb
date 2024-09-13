from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    CORS(app)

    # Import and register blueprints
    from .controller_credores import credores_bp
    from .controller_contas_a_pagar import contas_bp

    #app.register_blueprint(credor_bp, url_prefix='/credores')
    app.register_blueprint(contas_bp, url_prefix='/contas')
    app.register_blueprint(credores_bp,url_prefix='/credores')

    with app.app_context():
        db.create_all()

    return app
