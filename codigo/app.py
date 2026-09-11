from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

from config import Config
from extentions import db
app.config.from_object(Config)
db.init_app(app)

from models import *
from routes.usuarios import usuarios_bp
from routes.tarefas import tarefas_bp
from routes.apresentacao import apresentacao_bp
app.register_blueprint(usuarios_bp)
app.register_blueprint(tarefas_bp)
app.register_blueprint(apresentacao_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)