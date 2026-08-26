from flask import render_template, request, redirect, session, url_for, Blueprint
from models import Tarefas
from extentions import db
from datetime import datetime

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/tarefas', methods=['GET', 'POST'])
def tarefas():  
    if "usuario_id" not in session:
        return redirect(url_for('usuarios.login'))
    usuario_id = session["usuario_id"]
    tarefas = Tarefas.query.filter_by(usuario_id = usuario_id).all()
    
    return render_template('tarefas.html', tarefas=tarefas)

@tarefas_bp.route('/adicionar_tarefa', methods=['GET','POST'])
def adicionar_tarefa():

    if "usuario_id" not in session:
        return redirect(url_for('usuarios.login'))

    if request.method == 'POST':
        tarefa = request.form['tarefa']
        data = request.form['data']
        data_para_o_banco = datetime.strptime(data, "%Y-%m-%d").date()

        nova_tarefa = Tarefas (
            usuario_id = session["usuario_id"],
            tarefa = tarefa,
            data = data_para_o_banco ,
            estado = 'pendente'
        )

        db.session.add(nova_tarefa)
        db.session.commit()
        return redirect(url_for('tarefas.tarefas'))

    return render_template('adicionar_tarefa.html')