from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database, drop_database

from .extensions import db
from .views.main import main 

def create_app(environment=None):
    app = Flask(__name__)
    if environment == 'production':
        app.config.from_object('instance.config.ConfigProd')
    if environment == 'development':
        app.config.from_object('instance.config.ConfigDev')
    if environment == 'testing':
        pass

    register_extensions(app)
    app.register_blueprint(main, url_prefix='/')
    return app

def register_extensions(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()
