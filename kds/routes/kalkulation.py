from flask import Blueprint, redirect, render_template, request, url_for
from ..extensions import db
from ..models import TestTable

kalkulation = Blueprint('kalkulation', __name__)


@kalkulation.route('/', methods=['GET', 'POST'])
def index():
    """Default table view - show the table and provide form and
    functions for modifying that table.

    """
    table_data = TestTable.query.all()

    action = request.args.get('action')
    if action == 'add_row':
        return add_row()

    # else, show default template
    return render_template('kalkulation/index.html', data=table_data)

def add_row():
    """Show the template for adding table entries. """
    return render_template('kalkulation/add_row.html')