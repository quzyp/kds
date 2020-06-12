#!/usr/bin/env python

from flask import current_app
from .extensions import db 

class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=True)
    zipcode = db.Column(db.String(200), unique=False, nullable=True) 
    location = db.Column(db.String(200), unique=False, nullable=True)