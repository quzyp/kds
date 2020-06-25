# pylint: disable=C0415

""" Register the extensions. """

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def register_all(app):
    """ Register the extensions.

    :param app: The Flask app.
    :return: None
    """

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .models import Gewerk, Unternehmen

    admin = Admin(app, name='kds', template_mode='bootstrap3')
    admin.add_view(ModelView(Gewerk, db.session))
    admin.add_view(ModelView(Unternehmen, db.session))

