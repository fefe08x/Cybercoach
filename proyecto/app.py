# app.py
# Archivo principal de creación de la aplicación Flask

from flask import Flask
from flask_session import Session
from app.database import init_db
from config.config import get_config

def create_app():
    """
    Crea y configura la aplicación Flask.
    
    Returns:
        Flask: La aplicación configurada y lista para uso
    """
    app = Flask(__name__)
    
    # Configuración de la aplicación
    config_class = get_config()
    app.config.from_object(config_class)

    # Configurar Flask-Session
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = True
    app.config['PERMANENT_SESSION_LIFETIME'] = 1200  # 20 minutos en segundos
    Session(app)

    # Inicializar base de datos
    init_db(app)
    
    return app
