""" The main route. """

from flask import Blueprint, flash, g, redirect, render_template, request
from flask_babel import gettext
from sqlalchemy import exc

from flask_login import login_user, logout_user, current_user, login_required
from ..extensions import babel, db, login_manager
from ..forms import LoginForm, GewerkeForm, UnternehmenForm
from ..models import User, Gewerk, Unternehmen

main = Blueprint('main', __name__)
mapping = {'gewerke': {'model': Gewerk, 'form': GewerkeForm},
           'unternehmen': {'model': Unternehmen, 'form': UnternehmenForm}}
 
@babel.localeselector
def get_locale():
    return 'de'
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language
    return request.accept_languages.best_match(['de', 'en'])

@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(name=form.name.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                flash('Logged in successfully.', 'success')
                return redirect('/')
        flash('Wrong user or password.', 'warning')
        return redirect('/login')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """Default table view - show the table and provide form and
    functions for modifying that table.
    """
    return redirect('/gewerke')

@main.route('/<tablename>', methods=['GET', 'POST'])
@login_required
def tablepage(tablename):
    """ A generalized function for all data categories. """
    action = request.form.get('action', '')
    if tablename not in mapping:
        return '404'

    form = mapping[tablename]['form'](request.form)
    model = mapping[tablename]['model']

    if hasattr(form, 'gewerke'):
        # If the form expects gewerke for drop-down list, fill it from db.
        gewerke = [(g.id, g.titel) for g in Gewerk.query.all()]
        form.gewerke.choices = gewerke

    template_add = f'{tablename}/add.html'

    if action == 'form':
        return render_template(template_add, form=form)

    if action == 'add' and form.validate():
        if form.data['id'] == '0':
            # Get the table columns and fill with posted form data.
            table_columns = model.__dict__['__table__'].__dict__['_columns']
            columns = [x.name.split('.')[-1] for x in table_columns]
            columns.remove('id')
            fields = {x: form.data[x] for x in columns}
            row = model(**fields)
            db.session.add(row)
            try: # sqlalchemy throws exception when constrains are missed.
                db.session.commit()
                name = form.data[form.readable]
                flash(gettext(u'%(name)s added sucessfully.', name=name), 'success')
                for element in form: # set up a clean form
                    element.data = ''
                    form.id.data = '0'
            except exc.IntegrityError:
                form.index.errors.append(gettext(u'Invalid format or entry already in table.'))
            form = inject_css_on_error(form)
            return render_template(template_add, form=form)

    if action == 'add' and not form.validate():
        form = inject_css_on_error(form)
        return render_template(template_add, form=form)

    if not action:
        # Display the main table view.
        model = mapping[tablename]['model']
        table_data = model.query.all()
        template = f'{tablename}/index.html'
        return render_template(template, data=table_data)

def inject_css_on_error(form, css=' is-invalid'):
    """ Add a specific class to all form fields which have an error
    associated with it. The error comes from WTForms.
    """
    for field in form:
        try:
            classes = field.render_kw['class']
        except TypeError:
            continue
        if field.name in form.errors:
            field.render_kw['class'] = classes + css
        else:
            field.render_kw['class'] = classes.replace(css, '')
    return form
