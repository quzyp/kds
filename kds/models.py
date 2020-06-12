#!/usr/bin/env python
# pylint: disable=E1101

""" Module docstring. """

#from flask import current_app
from .extensions import db

class TestTable(db.Model):
    """ Class dostring. """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=True)
    zipcode = db.Column(db.String(200), unique=False, nullable=True)
    location = db.Column(db.String(200), unique=False, nullable=True)
