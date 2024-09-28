from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, migrate, bcrypt
from routes.registro_login import auth_bp
from middlewares.token_http import check_http_key
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configurar CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Configurar o logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app)
    bcrypt.init_app(app)

    # Registrar Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # Lista de rotas que não precisam de proteção
    app.config['PUBLIC_ROUTES'] = ['/api/auth/login']

    # Aplicar proteção a rotas específicas
    app.before_request(check_http_key)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)