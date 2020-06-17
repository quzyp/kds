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
    return redirect(url_for('gewerke.index'))

@main.route('/gew')
def gew():
    """Default table view - show the table and provide form and
    functions for modifying that table."""

    #Trade.query.delete()
    #Trade.__table__.drop(db.engine)
    #Trade.__table__.create(db.engine)


    #filepath = pathlib.Path(current_app.static_folder) / '_gewerke.txt'
    #with open(filepath, 'r', encoding='utf-8') as f:
    #    txt = f.readlines()
    #for line in txt:
    #    g = Trade(_index=line[:4], name=line[4:])
    #    db.session.add(g)
    #db.session.commit()
    #return ''
    
    trades = Trade.query.all()
    return '<br>'.join([f'{t._id}: {t.name}' for t in trades])
