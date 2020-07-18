# pylint: disable=C0415

""" Register the extensions. """

from flask import redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babel import Babel
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy

babel = Babel()
db = SQLAlchemy()
login_manager = LoginManager()

class AuthModelView(ModelView):
    """ Subclass of the standard flask-admin ModelView in order to
    provide access control. """

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/login')

def register_all(app):
    """ Register the extensions.

    :param app: The Flask app.
    :return: None
    """

    babel.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    from .models import User, Gewerk, Unternehmen

    admin = Admin(app, name='kds', template_mode='bootstrap3')
    admin.add_view(AuthModelView(Gewerk, db.session))
    admin.add_view(AuthModelView(Unternehmen, db.session))
    admin.add_view(AuthModelView(User, db.session))
