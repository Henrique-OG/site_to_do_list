from flask import render_template, request, redirect, session, url_for, Blueprint

apresentacao_bp = Blueprint('apresentacao', __name__)

@apresentacao_bp.route('/')
def apresentacao():
    if "usuario_id" in session:
        return redirect(url_for('tarefas.tarefas'))
    return render_template('inicio.html')

@apresentacao_bp.route('/sobre')
def sobre():
    if "usuario_id" in session:
        return redirect(url_for('tarefas.tarefas'))
    return render_template('sobre.html')