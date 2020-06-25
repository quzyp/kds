""" Import all blueprints and register them. """

from .main import main
from .gewerke import gewerke

def init_app(app):
    """ Register the blueprint. Used by the root __init__.

    :param app: The Flask app
    :return: None
    """

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(gewerke, url_prefix='/gewerke')
