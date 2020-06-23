""" Register the extensions. """

from flask import current_app as app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .models import Company, Trade

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Company, db.session))
admin.add_view(ModelView(Trade, db.session))
