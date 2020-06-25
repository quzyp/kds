""" Module docstring. """

from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy import exc

from ..extensions import db
from ..models import Gewerk
from ..forms import GewerkeForm

gewerke = Blueprint('gewerke', __name__)

@gewerke.route('/', methods=['GET', 'POST'])
def index():
    """Default table view - show the table and provide form and
    functions for modifying that table.

    """

    action = request.form.get('action')
    if not action:
        action = request.args.get('action')

    if action == 'delete':
        id_ = int(request.args.get('id'))
        Gewerk.query.filter_by(id=id_).delete()
        db.session.commit()

    table_data = Gewerk.query.all()

    # else, show default template
    return render_template('gewerke/index.html', data=table_data)

@gewerke.route('/add', methods=['GET', 'POST'])
def add():
    form = GewerkeForm(request.form)

    if request.method == 'POST' and form.validate():
        index_ = request.form['index']
        titel = request.form['titel']
        t = Gewerk(index=index_, titel=titel)
        db.session.add(t)
        try:
            db.session.commit()
            flash(f'"{titel}" erfolgreich hinzugefügt.', 'success')
            form.index.data = ''
            form.titel.data = ''
        except exc.IntegrityError:
            form.index.errors.append(f'Index {index_} bereits vorhanden.')
    form = inject_css_on_error(form)
    return render_template('gewerke/add.html', form=form)

def inject_css_on_error(form, css=' is-invalid'):
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