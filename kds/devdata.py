""" Load filler data for development. """

import pathlib

from .models import User, Gewerk, Unternehmen
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
                for i in range(len(values)):
                    if values[i].startswith('['):
                        values[i] = eval(values[i])
                db.session.add(table(**dict(zip(keys, values))))
            db.session.commit()
        u = User(name='admin')
        u.set_password('admin007')
        db.session.add(u)
        db.session.commit()
