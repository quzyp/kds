""" Load filler data for development. """

import pathlib

from .models import Gewerk, Unternehmen
from .extensions import db

def filldb(app):
    tables = [Gewerk, Unternehmen]
    with app.app_context():
        for table in tables:
            name = table.__tablename__
            columns = [x.name for x in table.__table__._columns]
            keys = [x.split('.')[-1] for x in columns[1:]]
            filepath = pathlib.Path(app.static_folder) / 'devdata' / f'{name}.txt'
            with open(filepath, 'r', encoding='utf-8') as file_:
                txt = file_.readlines()
            for line in txt:
                values = line.split('|')
                db.session.add(table(**dict(zip(keys, values))))
            db.session.commit()
