""" The main route. """

import pathlib

from flask import Blueprint, current_app, redirect, url_for

from ..extensions import db
from ..models import Unternehmen, Gewerk

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    """Default table view - show the table and provide form and
    functions for modifying that table.

    """
    return redirect(url_for('gewerke.index'))

@main.route('/gew')
def gew():
    """Drop and regenerate gewerke table from file. """

    Gewerk.query.delete()
    Gewerk.__table__.drop(db.engine)
    Gewerk.__table__.create(db.engine)

    filepath = pathlib.Path(current_app.static_folder) / '_gewerke.txt'
    with open(filepath, 'r', encoding='utf-8') as file_:
        txt = file_.readlines()
    for line in txt:
        row = Gewerk(index=line[:4], titel=line[4:])
        db.session.add(row)
    db.session.commit()
    return 'Created gewerke table from file.'
