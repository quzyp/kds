""" Module docstring. """

from flask import Blueprint, render_template, request
from sqlalchemy import exc

from ..extensions import db
from ..models import Trade

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
        _index = request.form['_index']
        name = request.form['name']
        t = Trade(_index=_index, name=name)
        db.session.add(t)
        try:
            db.session.commit()
        except exc.IntegrityError:
            return render_template('gewerke/add_row.html', form=request.form, msg=[{'error': 'Index bereits vorhanden!'}])

    if action == 'delete':
        _id = int(request.args.get('id'))
        Trade.query.filter_by(_id=_id).delete()
        db.session.commit()

    table_data = Trade.query.all()

    # else, show default template
    return render_template('gewerke/index.html', data=table_data)

@gewerke.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('gewerke/add.html', form={}, msg={})
