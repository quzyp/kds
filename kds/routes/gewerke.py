""" Module docstring. """

from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy import exc

from ..extensions import db
from ..models import Trade
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

    if action == 'add':
        get_args = {}
        _index = request.form['_index']
        name = request.form['name']
        t = Trade(_index=_index, name=name)
        db.session.add(t)
        try:
            db.session.commit()
            flash(f'"{name}" erfolgreich hinzugefügt.', 'success')
        except exc.IntegrityError:
            flash('Index bereits vorhanden.', 'danger')
            get_args['_index-class'] = 'is-invalid'#
            get_args['_index-text'] = _index
            get_args['name-text'] = name
        return redirect(url_for('gewerke.add', **get_args))

    if action == 'delete':
        _id = int(request.args.get('id'))
        Trade.query.filter_by(_id=_id).delete()
        db.session.commit()

    table_data = Trade.query.all()

    # else, show default template
    return render_template('gewerke/index.html', data=table_data)

@gewerke.route('/add', methods=['GET', 'POST'])
def add():
    form = GewerkeForm(request.form)

    if request.method == 'POST' and form.validate():
        pass
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