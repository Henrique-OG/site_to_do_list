from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site_to_do_list.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
