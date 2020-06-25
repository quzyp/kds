# disable pylint check for import outside top-level.
# pylint: disable=C0415

""" The main setup. Import all parts and register extensions. """

from flask import Flask


def create_app(environment=None):
    """ The app factory.

    :param str environment: The environment the app should run in.
    :return: The Flask aoo
    """
    from . import extensions, routes

    app = Flask(__name__)

    if environment == 'dev':
        app.config.from_object('kds.config.ConfigDev')

    if environment == 'production':
        app.config.from_object('instance.config.ConfigProd')

    if environment == 'testing':
        print('### Testing not implemented. ###')
        return

    extensions.register_all(app)
    routes.init_app(app)

    return app
