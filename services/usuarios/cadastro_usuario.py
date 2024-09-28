from models.usuario import Usuario
from extensions import db
import re

def senha_forte(senha):
    """
    Verifica se a senha é forte o suficiente.
    Requer pelo menos 8 caracteres, uma letra maiúscula, uma minúscula, um número e um caractere especial.
    """
    if len(senha) < 8:
        return False
    if not re.search(r"[A-Z]", senha):
        return False
    if not re.search(r"[a-z]", senha):
        return False
    if not re.search(r"\d", senha):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False
    return True

def cadastrar_usuario(nome, usuario, senha):
    # Verifica se o usuário já existe
    if Usuario.query.filter_by(usuario=usuario).first():
        return {"error": "Usuário já existe"}, 400

    # Verifica se a senha é forte
    if not senha_forte(senha):
        return {"error": "Senha fraca. A senha deve ter pelo menos 8 caracteres, incluindo maiúsculas, minúsculas, números e caracteres especiais."}, 400

    # Cria um novo usuário
    novo_usuario = Usuario(nome=nome, usuario=usuario, senha=senha)

    try:
        db.session.add(novo_usuario)
        db.session.commit()
        return {"message": "Usuário cadastrado com sucesso"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500