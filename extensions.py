from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt  # Importar o Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()  # Inicializar o Bcrypt
