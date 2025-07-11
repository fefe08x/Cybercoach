# app.py
# Archivo principal de la aplicación Flask
# Este archivo se encarga de la configuración inicial y la creación de la aplicación
# Sigue el patrón de aplicación de fábrica para facilitar la configuración y el testing

import os
from flask import Flask
from dotenv import load_dotenv
from app.database import init_db

# Carga de configuraciones
# ========================================
# Utilizamos dotenv para manejar variables de entorno de manera segura
# Esto permite:
# - Mantener credenciales fuera del código
# - Facilitar el despliegue en diferentes entornos
# - Seguir las mejores prácticas de seguridad
load_dotenv()

# Configuración de seguridad
# ========================================
# Clave secreta para la aplicación
# Se recomienda usar una clave más robusta en producción
# La clave por defecto es solo para desarrollo
CLAVE_SECRETA = os.getenv('SECRET_KEY', 'clave-secreta-por-defecto')

# Configuración de la base de datos
# ========================================
# Configuración centralizada para PostgreSQL
# Todas las credenciales se obtienen del archivo .env
# Esto sigue las mejores prácticas de seguridad
# Las variables por defecto son para desarrollo local
DB_CONFIG = {
    'usuario': os.getenv('DB_USUARIO', 'postgres'),
    'contrasena': os.getenv('DB_CONTRASEÑA', 'awds'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'puerto': os.getenv('DB_PUERTO', '5432'),
    'nombre': os.getenv('DB_NOMBRE', 'cybercoach_db')
}

def create_app():
    """
    Función que crea y configura la aplicación Flask
    
    Returns:
        Flask: La aplicación configurada y lista para uso
    
    Notas:
    - Usa el patrón de aplicación de fábrica
    - Configura la base de datos con SQLAlchemy
    - Establece la clave secreta para sesiones
    """
    # Crear la aplicación
    app = Flask(__name__)
    
    # Configurar la clave secreta
    app.config['SECRET_KEY'] = CLAVE_SECRETA

    # Configurar la base de datos
    # ========================================
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f'postgresql://{DB_CONFIG["usuario"]}:{DB_CONFIG["contrasena"]}'
        f'@{DB_CONFIG["host"]}:{DB_CONFIG["puerto"]}/{DB_CONFIG["nombre"]}'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos
    # ========================================
    init_db(app)
    
    # Verificar que las tablas existan
    with app.app_context():
        from app.models import Usuario, Ejercicio, EjercicioEnRutina
        db.create_all()

    # Registro de blueprints y configuraciones adicionales
    # ========================================
    # En un proyecto más grande, aquí registraríamos los blueprints
    # y configuraríamos middleware, interceptores, etc.
    
    return app

if __name__ == '__main__':
    # Crear y ejecutar la aplicación
    # Modo debug activado para desarrollo
    app = create_app()
    app.run(debug=True)
