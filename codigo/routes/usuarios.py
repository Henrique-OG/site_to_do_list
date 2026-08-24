from flask import render_template, request, redirect, url_for, Blueprint
from models import Usuarios
from extentions import db

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']


        if Usuarios.query.filter((Usuarios.nome_usuario == nome) | (Usuarios.email_usuario == email)).first():
            return render_template('cadastro.html', erro='Nome de usuário ou email já existe.')

        novo_usuario = Usuarios(
            nome_usuario=nome,
            email_usuario=email,
            senha_usuario=senha
        )
        
        db.session.add(novo_usuario)
        db.session.commit()

    return render_template('cadastro.html')

@usuarios_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')