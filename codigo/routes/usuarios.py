from flask import render_template, request, redirect, session, url_for, Blueprint
from models import Usuarios
from extentions import db
from werkzeug.security import generate_password_hash, check_password_hash

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)


        if Usuarios.query.filter((Usuarios.nome_usuario == nome) | (Usuarios.email_usuario == email)).first():
            return render_template('cadastro.html', erro='Nome de usuário ou email já existe.')

        novo_usuario = Usuarios(
            nome_usuario=nome,
            email_usuario=email,
            senha_usuario=senha_hash
        )
        
        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for('usuarios.login'))

    return render_template('cadastro.html')

@usuarios_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        usuario = Usuarios.query.filter_by(nome_usuario=nome).first()

        if usuario and check_password_hash(usuario.senha_usuario, senha):
            session['usuario_id'] = usuario.id
            return redirect(url_for('tarefas.tarefas'))
        else:
            return render_template('login.html', erro='Nome de usuário ou senha incorretos.')

    return render_template('login.html')

@usuarios_bp.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('usuarios.login'))
