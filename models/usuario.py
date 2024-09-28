# models/usuario.py
from extensions import db, bcrypt

class Usuario(db.Model):
    __tablename__ = 'usuario'  # Alinhado com o banco

    ID_usuario = db.Column(db.Integer, primary_key=True)  # Alinhado com o banco
    nome = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

    def verificar_senha(self, senha):
        return bcrypt.check_password_hash(self.senha_hash, senha)