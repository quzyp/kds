""" Module docstring. """

from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy import exc

from ..extensions import db
from ..models import Gewerk, Unternehmen
from ..forms import UnternehmenForm

unternehmen = Blueprint('Unternehmen', __name__)

@unternehmen.route('/', methods=['GET', 'POST'])
def index():
    """Default table view - show the table and provide form and
    functions for modifying that table.

    """

    action = request.form.get('action')
    if not action:
        action = request.args.get('action')

    if action == 'delete':
        id_ = int(request.args.get('id'))
        Unternehmen.query.filter_by(id=id_).delete()
        db.session.commit()

    table_data = Unternehmen.query.all()

    # else, show default template
    return render_template('unternehmen/index.html', data=table_data)

@unternehmen.route('/add', methods=['GET', 'POST'])
def add():
    form = UnternehmenForm(request.form)
    gewerke = [(g.id, g.titel) for g in Gewerk.query.all()]
    form.gewerke.choices = gewerke

    if request.method == 'POST' and form.validate():
        name = request.form['name']
        adr_strasse = request.form['adr_strasse']
        adr_plz = request.form['adr_plz']
        adr_stadt = request.form['adr_stadt']
        gewerke = request.form.getlist('gewerke')
        gewerke = [Gewerk.query.get(int(x)) for x in gewerke]
        t = Unternehmen(name=name, adr_strasse=adr_strasse, adr_plz=adr_plz, adr_stadt=adr_stadt, gewerke=gewerke)
        db.session.add(t)
        try:
            db.session.commit()
            flash(f'"{name}" erfolgreich hinzugefügt.', 'success')
            form.name.data = ''
            form.adr_stadt.data = ''
        except exc.IntegrityError:
            form.index.errors.append(f'"{name}" bereits vorhanden.')
    form = inject_css_on_error(form)
    return render_template('unternehmen/add.html', form=form)

def inject_css_on_error(form, css=' is-invalid'):
    for field in form:
        try:
            classes = field.render_kw['class']
        except KeyError:
            continue
        if field.name in form.errors:
            field.render_kw['class'] = classes + css
        else:
            field.render_kw['class'] = classes.replace(css, '')
    return form