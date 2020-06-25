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

    configs = {'dev': (lambda: app.config.from_object('kds.config.ConfigDev')),
               'prod': (lambda: app.config.from_object('instance.config.ConfigProd')),
               'testing': (lambda: app.config.from_object('kds.config.ConfigTesting'))}
    try:
        configs[environment]()
    except KeyError:
        print(f'### Invalid FLASK_ENV: {environment} ###')
        return

    extensions.register_all(app)
    routes.init_app(app)

    return app
