import pathlib
from flask import Blueprint, current_app, redirect, render_template, request, url_for
from ..extensions import db
from ..models import TestTable, Trade

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    """Default table view - show the table and provide form and
    functions for modifying that table.

    """
    return redirect(url_for('kalkulation.index'))

@main.route('/gew')
def gew():
    """Default table view - show the table and provide form and
    functions for modifying that table.

    
    filepath = pathlib.Path(current_app.static_folder) / '_gewerke.txt'
    with open(filepath, 'r') as f:
        txt = f.readlines()
    for line in txt:
        g = Trade(name=line[4:])
        db.session.add(g)
    db.session.commit()
    return ''
    """
    trades = Trade.query.all()
    return '<br>'.join([f'{t._id}: {t.name}' for t in trades])
