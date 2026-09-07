from flask import render_template, request, redirect, session, url_for, Blueprint
from models import Tarefas
from extentions import db
from datetime import datetime
from sqlalchemy import case

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/tarefas', methods=['GET', 'POST'])
def tarefas():  
    if "usuario_id" not in session:
        return redirect(url_for('usuarios.login'))
    usuario_id = session["usuario_id"]
    filtro = request.args.get('filtro')
    if filtro == 'pendentes':
        tarefas = Tarefas.query.filter_by(usuario_id = usuario_id, estado='pendente').all()
    elif filtro == 'concluidas':
        tarefas = Tarefas.query.filter_by(usuario_id = usuario_id, estado='concluida').all()
    else:
        tarefas = Tarefas.query.filter_by(usuario_id = usuario_id).order_by(
            case(
                (Tarefas.estado == 'pendente', 1),
                (Tarefas.estado == 'concluida', 2)
            )
        ).all()
    
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

@tarefas_bp.route('/excluir_tarefa/<int:id>')
def excluir_tarefa(id):
    if "usuario_id" not in session:
        return redirect(url_for('usuarios.login'))

    usuario_id = session['usuario_id']
    tarefa = Tarefas.query.get(id)
    if usuario_id == tarefa.usuario_id:
        db.session.delete(tarefa)
        db.session.commit() 
    else:
        return redirect(url_for('tarefas.tarefas'))

    return redirect(url_for('tarefas.tarefas'))

@tarefas_bp.route('/editar_tarefa/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
    if "usuario_id" not in session:
        return redirect(url_for('usuarios.login'))

    usuario_id = session['usuario_id']
    tarefa = Tarefas.query.get(id)
    if usuario_id != tarefa.usuario_id:
        return redirect(url_for('tarefas.tarefas'))
    

    if request.method == 'POST':
        tarefa.tarefa = request.form['tarefa']
        tarefa.data = datetime.strptime(request.form['data'], "%Y-%m-%d").date()
        db.session.commit()
        return redirect(url_for('tarefas.tarefas'))

    return render_template('editar_tarefa.html', tarefa=tarefa)

@tarefas_bp.route('/concluir_tarefa/<int:id>', methods=['POST'])
def concluir_tarefa(id):
    if "usuario_id" not in session:
        return redirect(url_for('usuarios.login'))

    usuario_id = session['usuario_id']
    tarefa = Tarefas.query.get(id)
    if usuario_id == tarefa.usuario_id:
        if tarefa.estado == 'pendente':
            tarefa.estado = 'concluida'
            db.session.commit()
        else:
            tarefa.estado = 'pendente'
            db.session.commit()
    else:
        return redirect(url_for('tarefas.tarefas'))

    return redirect(url_for('tarefas.tarefas'))