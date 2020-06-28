""" Import all blueprints and register them. """

from .main import main
from .gewerke import gewerke
from .unternehmen import unternehmen

def init_app(app):
    """ Register the blueprint. Used by the root __init__.

    :param app: The Flask app
    :return: None
    """

    app.register_blueprint(main, url_prefix='/')
    #app.register_blueprint(gewerke, url_prefix='/gewerke')
    #app.register_blueprint(unternehmen, url_prefix='/unternehmen')
