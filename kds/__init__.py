""" The main setup. Import views and register extensions. """

from flask import Flask

from .extensions import admin, db
from .views.main import main
from .views.kalkulation import kalkulation
from .views.gewerke import gewerke

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
    app.register_blueprint(kalkulation, url_prefix='/kalkulation')
    app.register_blueprint(gewerke, url_prefix='/gewerke')

    return app

def register_extensions(app):
    db.init_app(app)
    
