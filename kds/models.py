""" Module docstring. """

#from flask import current_app
from .extensions import db

class TestTable(db.Model):
    """ Class dostring. """
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=True)
    zipcode = db.Column(db.String(200), unique=False, nullable=True)
    location = db.Column(db.String(200), unique=False, nullable=True)

class Company(db.Model):
    """ Table for a company. """
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    street = db.Column(db.String(200), unique=False, nullable=True)
    zipcode = db.Column(db.String(200), unique=False, nullable=True)
    city = db.Column(db.String(200), unique=False, nullable=True)
    phone = db.Column(db.String(200), unique=False, nullable=True)
    fax = db.Column(db.String(200), unique=False, nullable=True)
    trade = db.Column(db.String(200), unique=False, nullable=True)

class Trade(db.Model):
    """ Trade. """
    _id = db.Column(db.Integer, primary_key=True)
    _index = db.Column(db.String(3), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
