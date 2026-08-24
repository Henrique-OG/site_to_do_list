from extentions import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(100), nullable=False, unique=True)
    email_usuario = db.Column(db.String(100), nullable=False, unique=True)
    senha_usuario = db.Column(db.String(100), nullable=False)
    