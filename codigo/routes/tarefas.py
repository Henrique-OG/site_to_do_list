from flask import render_template, request, redirect, session, url_for, Blueprint
from models import Usuarios
from extentions import db

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/tarefas', methods=['GET', 'POST'])
def tarefas():  
    if "usuario_id" not in session:
        return redirect(url_for('usuarios.login'))
    usuario_id = session["usuario_id"]
    nome_usuario = Usuarios.query.get(usuario_id).nome_usuario
    
    return render_template('tarefas.html', nome_usuario=nome_usuario)