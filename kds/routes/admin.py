#!/usr/bin/env python

""" Module docstring."""

import random
from flask import Blueprint, redirect, render_template, url_for
from ..extensions import db
from ..models import TestTable

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return str(TestTable.__dict__)

@admin.route('/add')
def add():
    name = ''.join([random.choice('Mike Peter Monday') for x in range(13)])
    t = TestTable(name=name, zipcode='12345', location='Fake Str')
    db.session.add(t)
    db.session.commit()
    return redirect(url_for('admin.index'))