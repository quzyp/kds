""" The main route. """

import pathlib

from flask import Blueprint, current_app, redirect, render_template, request, url_for

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
    action = request.form.get('action', '')
    form = mapping[tablename]['form'](request.form)

    if action == 'form':
        template = f'{tablename}/add.html'
        return render_template(template, form=form)

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
            except exc.IntegrityError:
                form.index.errors.append(f'Index {index_} bereits vorhanden.')
            form = inject_css_on_error(form)
            return render_template(template, form=form)

    table_data = mapping[tablename]['model'].query.all()
    template = f'{tablename}/index.html'
    return render_template(template, data=table_data)
