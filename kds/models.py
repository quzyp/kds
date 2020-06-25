""" Module docstring. """

from .extensions import db

unt_gew = db.Table('unt_gew',
                   db.Column('unt_id', db.Integer, db.ForeignKey('unternehmen.id'), primary_key=True),
                   db.Column('gew_id', db.Integer, db.ForeignKey('gewerk.id'), primary_key=True),
)

class Unternehmen(db.Model):
    """ Table for a company. """

    __tablename__ = 'unternehmen'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    adr_strasse = db.Column(db.String(200), unique=False, nullable=True)
    adr_plz = db.Column(db.String(200), unique=False, nullable=True)
    adr_stadt = db.Column(db.String(200), unique=False, nullable=True)
    con_fon = db.Column(db.String(200), unique=False, nullable=True)
    con_fax = db.Column(db.String(200), unique=False, nullable=True)
    gewerke = db.relationship('Gewerk', secondary=unt_gew, lazy='subquery',
                              backref=db.backref('unternehmen', lazy=True))


class Gewerk(db.Model):
    """ Trade. """

    __tablename__ = 'gewerk'

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String(3), unique=True, nullable=False)
    titel = db.Column(db.String(255), unique=True, nullable=False)
