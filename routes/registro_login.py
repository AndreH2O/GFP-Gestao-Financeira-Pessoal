from flask import Blueprint, request, jsonify
from services.usuarios.cadastro_usuario import cadastrar_usuario
from services.usuarios.login import efetuar_login

# Definir o Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/cadastro', methods=['POST'])
def registro():
    data = request.get_json()
    nome = data.get('nome')
    usuario = data.get('usuario')
    senha = data.get('senha')

    if not all([nome, usuario, senha]):
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    return cadastrar_usuario(nome, usuario, senha)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    senha = data.get('senha')

    if not all([usuario, senha]):
        return jsonify({"error": "Usuário e senha são obrigatórios"}), 400

    result, status_code = efetuar_login(usuario, senha)
    return jsonify(result), status_code