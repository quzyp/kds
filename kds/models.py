""" ALl the database models go here. """

import hmac
import os
from hashlib import pbkdf2_hmac

from flask_login import UserMixin

from .extensions import db

unt_gew = db.Table('unt_gew',
                   db.Column('unt_id',
                             db.Integer,
                             db.ForeignKey('unternehmen.id'),
                             primary_key=True),
                   db.Column('gew_id',
                             db.Integer,
                             db.ForeignKey('gewerk.id'),
                             primary_key=True))

class User(UserMixin, db.Model):
    """ The User class. set_password and check_password are defined here as
    this is the only model where those are needed.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(64))
    salt = db.Column(db.String(32))

    def set_password(self, password):
        """Create hashed password."""
        salt = os.urandom(16)
        self.salt = salt.hex()
        self.password = pbkdf2_hmac('sha256',
                                    password.encode(),
                                    salt,
                                    100_000).hex()

    def check_password(self, password):
        """Check hashed password."""
        return hmac.compare_digest(bytes.fromhex(self.password),
                                   pbkdf2_hmac('sha256',
                                               password.encode(),
                                               bytes.fromhex(self.salt),
                                               100_000))

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Unternehmen(db.Model):
    """ Table for a company. """

    __tablename__ = 'unternehmen'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    adr_strasse = db.Column(db.String(200), unique=False, nullable=False)
    adr_plz = db.Column(db.String(200), unique=False, nullable=False)
    adr_stadt = db.Column(db.String(200), unique=False, nullable=False)
    con_fon = db.Column(db.String(200), unique=False, nullable=True)
    con_fax = db.Column(db.String(200), unique=False, nullable=True)
    gewerke = db.relationship('Gewerk', secondary=unt_gew, lazy='subquery',
                              backref=db.backref('unternehmen', lazy=True))


class Gewerk(db.Model):
    """ Trade. """

    __tablename__ = 'gewerk'

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String(3), unique=True, nullable=False)
    titel = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return str(self.titel)
