
from flask import Blueprint, redirect, render_template, url_for
from ..extensions import db
from ..models import TestTable

main = Blueprint('main', __name__)


@main.route('/')
def index():
    data = TestTable.query.all()
    return render_template('index/index.html', data=data)

@main.route('/reset')
def reset():
    #Drop database and create a fresh one, including tables.
    if database_exists(DB_URL):
        drop_database(DB_URL)
    create_database(DB_URL)
    db.create_all()
    return redirect(url_for('index/index'))

@main.route('/dummy')
def dummy():
    abc = TestTable(name='ABC GmbH', zipcode='01446', location='Berlin')
    foobar = TestTable(name='foobar AG', zipcode='45329', location='Essen')
    db.session.add(abc)
    db.session.add(foobar)
    db.session.commit()
    return redirect(url_for('index/index'))