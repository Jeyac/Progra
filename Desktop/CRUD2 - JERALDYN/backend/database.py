import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde el archivo .env

db = SQLAlchemy()  # Crear objeto para manejar la base de datos

def init_app(app):
    # Configurar la conexión a PostgreSQL usando las variables del .env
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactiva seguimiento innecesario
    db.init_app(app)  # Vincular la base de datos con la app Flask
