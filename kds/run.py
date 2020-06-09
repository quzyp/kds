from flask import Flask, render_template
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


class Nachunternehmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=True)
    ort = db.Column(db.String(200), unique=False, nullable=True)


@app.route('/')
def root():
    sre = Nachunternehmer(name='SRE GmbH', ort='Rostock')
    kempf = Nachunternehmer(name='Kempf elektrobau GmbH', ort='Büren')
    db.session.add(sre)
    db.session.add(kempf)
    db.session.commit()

    return render_template('index.html', nu=Nachunternehmer.query.all())

@app.route('/reset')
def reset():
    if database_exists(DB_URL):
        drop_database(DB_URL)
    create_database(DB_URL)
    #db.drop_all()
    db.create_all()
    return 'Ok.'

if __name__ == '__main__':
    app.debug = True
    app.run()