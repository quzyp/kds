#!/usr/bin/env python
 
import os
import pathlib
import subprocess
import sys
import datetime

from kds import create_app

project_root = pathlib.Path(__file__).resolve().parent

if __name__ == '__main__':
    operation = sys.argv[-1]
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    if len(sys.argv) == 1:
        os.environ['FLASK_ENV'] = 'development'
        app = create_app('development')
        app.run()
    
    if operation == 'coverage':
        output = project_root / 'dev' / f'coverage_report_{now}'
        htmlcov = project_root / 'dev' / 'htmlcov'
        os.environ['COVERAGE_FILE'] = str(output)
        cmd = f'coverage run -m unittest discover'
        subprocess.call(cmd, shell=True)
        cmd = f'coverage html -d {htmlcov} --omit="venv/*"'
        subprocess.call(cmd, shell=True)

    if operation == 'pylint':
        rcfile = project_root / '.pylintrc'
        output = project_root / 'dev' / f'pylint_report_{now}'
        cmd = f'pylint kds --rcfile {rcfile} > {output}'
        subprocess.call(cmd, shell=True)

    if operation == 'test':
        print('Tests not implemented yet.')
