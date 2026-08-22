from flask import render_template, request, redirect, url_for, Blueprint
from models import Usuarios

usuarios_bp = Blueprint('usuarios', __name__)