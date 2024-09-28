import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env


class Config:
    HTTP_KEY = os.getenv('HTTP_KEY')
    if not HTTP_KEY:
        raise ValueError("HTTP_KEY não está definida no arquivo .env") # dep

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Adicione um print para debug
    print(f"HTTP_KEY carregada: {HTTP_KEY}")