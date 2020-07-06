""" The main route. """

import pathlib

from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from sqlalchemy import exc

from ..extensions import db
from ..models import Unternehmen, Gewerk
from ..forms import GewerkeForm, UnternehmenForm

main = Blueprint('main', __name__)
mapping = {'gewerke': {'model': Gewerk, 'form': GewerkeForm},
           'unternehmen': {'model': Unternehmen, 'form': UnternehmenForm}}

@main.route('/', methods=['GET', 'POST'])
def index():
    """Default table view - show the table and provide form and
    functions for modifying that table.

    """
    #return redirect(url_for('gewerke.index'))
    return redirect('/gewerke')

@main.route('/<tablename>', methods=['GET', 'POST'])
def tablepage(tablename):
    """ A generalized function for all data categories. """
    action = request.form.get('action', '')
    form = mapping[tablename]['form'](request.form)

    template_add = f'{tablename}/add.html'

    if action == 'form':
        return render_template(template_add, form=form)

    if action == 'add' and form.validate():
        if form.data['id'] == '0':
            # FIXME: these three lines filte the form dict so that only 
            # real db columns are passed. Ugly.
            columns = [x.name.split('.')[-1] for x in Gewerk.__dict__['__table__'].__dict__['_columns']]
            columns.remove('id')
            fields = {x: form.data[x] for x in columns}
            row = mapping[tablename]['model'](**fields)
            db.session.add(row)
            try:
                db.session.commit()
                name = form.data[form.readable]
                flash(f'"{name}" erfolgreich hinzugefügt.', 'success')
                for element in form: # set up a clean form
                    element.data = ''
                    form.id.data = '0'
            except exc.IntegrityError:
                form.index.errors.append('Eintrag bereits vorhanden oder ungültig.')
            form = inject_css_on_error(form)
            return render_template(template_add, form=form)

    if action == 'add' and not form.validate():
        form = inject_css_on_error(form)
        return render_template(template_add, form=form)

    if not action:
        # Display the main table view.
        table_data = mapping[tablename]['model'].query.all()
        template = f'{tablename}/index.html'
        return render_template(template, data=table_data)

 
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