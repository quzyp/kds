#!/usr/bin/env python

""" The admin route, nothing to see here."""

from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return ''
