from flask import Flask
from pymongo import MongoClient
import os

app = Flask('inmobiliary')

mongo = MongoClient(os.getenv('MONGO_URI'))

# Registra Blueprint
from routes import inmobiliary_bp
from models import Inmobiliary

# Función para configurar la aplicación
def configure_app():
    app.inmobiliary_model = Inmobiliary(mongo[os.getenv('DATABASE_NAME')])

# Llamamos a la función de configuración
configure_app()

app.register_blueprint(inmobiliary_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
