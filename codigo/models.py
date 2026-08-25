from extentions import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(100), nullable=False, unique=True)
    email_usuario = db.Column(db.String(100), nullable=False, unique=True)
    senha_usuario = db.Column(db.String(100), nullable=False)

class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    tarefa = db.Column(db.String(200), nullable=False)
    data = db.Column(db.DateTime)
    estado = db.Column(db.String(20), default='pendente')
