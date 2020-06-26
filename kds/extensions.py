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

    if app.env == 'dev':
        with app.app_context():
            mock = Gewerk(index='123', titel='Betonarbeiten')
            db.session.add(mock)
            mock = Gewerk(index='210', titel='Starkstrom')
            db.session.add(mock)
            db.session.commit()

    admin = Admin(app, name='kds', template_mode='bootstrap3')
    admin.add_view(ModelView(Gewerk, db.session))
    admin.add_view(ModelView(Unternehmen, db.session))
