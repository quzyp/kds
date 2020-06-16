from flask import Blueprint, redirect, render_template, request, url_for
from ..extensions import db
from ..models import Trade

gewerke = Blueprint('gewerke', __name__)


@gewerke.route('/', methods=['GET', 'POST'])
def index():
    """Default table view - show the table and provide form and
    functions for modifying that table.

    """
    table_data = Trade.query.all()

    action = request.args.get('action')
    if action == 'add_row':
        return add_row()

    # else, show default template
    return render_template('gewerke/index.html', data=table_data)

def add_row():
    """Show the template for adding table entries. """
    return render_template('gewerke/add_row.html')