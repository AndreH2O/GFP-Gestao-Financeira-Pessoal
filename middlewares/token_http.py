from flask import request, jsonify, current_app
import logging

logger = logging.getLogger(__name__)

def check_http_key():
    if request.path in current_app.config['PUBLIC_ROUTES']:
        return None

    possible_header_names = ['HTTP_KEY', 'Http-Key', 'Http_Key', 'X-HTTP-KEY', 'X-Http-Key']
    http_key = next((request.headers.get(name) for name in possible_header_names if request.headers.get(name)), None)

    expected_key = current_app.config.get('HTTP_KEY')
    if not http_key or http_key != expected_key:
        logger.warning("Tentativa de acesso com chave de autenticação inválida ou ausente")
        return jsonify({"error": "Chave de autenticação inválida ou ausente"}), 401
    return None