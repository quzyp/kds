from flask import Blueprint, redirect, render_template, request, url_for
from sqlalchemy import exc

from ..extensions import db
from ..models import Trade

gewerke = Blueprint('gewerke', __name__)


@gewerke.route('/', methods=['GET', 'POST'])
def index():
    """Default table view - show the table and provide form and
    functions for modifying that table.

    """
    table_data = Trade.query.all()

    action = request.form.get('action')
    if not action:
        action = request.args.get('action')

    if action == 'add_row':
        return render_template('gewerke/add_row.html')

    if action == 'add':
        _index = request.form['_index']
        name = request.form['name']
        t = Trade(_index=_index, name=name)
        db.session.add(t)
        try:
            db.session.commit()
        except exc.IntegrityError:
            return 'Nope'
        table_data = Trade.query.all()

    # else, show default template
    return render_template('gewerke/index.html', data=table_data)
