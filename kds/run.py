from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database, drop_database

PG_USER = 'postgres'
PG_PW = 'n2gether'
PG_URL = '127.0.0.1:5432'
PG_DB = 'kds'
DB_URL = f'postgresql+psycopg2://{PG_USER}:{PG_PW}@{PG_URL}/{PG_DB}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)

class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=True)
    zipcode = db.Column(db.String(200), unique=False, nullable=True) 
    location = db.Column(db.String(200), unique=False, nullable=True)


@app.route('/')
def index():
    data = TestTable.query.all()
    return render_template('index.html', data=data)

@app.route('/reset')
def reset():
    ''' Drop database and create a fresh one, including tables.'''
    if database_exists(DB_URL):
        drop_database(DB_URL)
    create_database(DB_URL)
    db.create_all()
    return redirect(url_for('index'))

@app.route('/dummy')
def dummy():
    abc = TestTable(name='ABC GmbH', zipcode='01446', location='Berlin')
    foobar = TestTable(name='foobar AG', zipcode='45329', location='Essen')
    db.session.add(abc)
    db.session.add(foobar)
    db.session.commit()
    return redirect(url_for('index'))
                    
if __name__ == '__main__':
    app.debug = True
    app.run()
