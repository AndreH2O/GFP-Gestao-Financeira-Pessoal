# services/usuarios/login.py
from models.usuario import Usuario

def efetuar_login(usuario, senha):
    user = Usuario.query.filter_by(usuario=usuario).first()

    if user and user.verificar_senha(senha):
        return {
            "mensagem": "Login bem-sucedido",
            "nome": user.nome,
            "usuario": user.usuario
        }, 200

    return {"error": "Usuário ou senha inválidos"}, 401