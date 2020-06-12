#!/usr/bin/env python

import os
import pathlib
import subprocess
import sys
import time

from kds import create_app

project_root = pathlib.Path(__file__).resolve().parent

if __name__ == '__main__':
    operation = sys.argv[-1]

    if len(sys.argv) == 1:
        os.environ['FLASK_ENV'] = 'development'
        app = create_app('development')
        app.run()
    
    if operation == 'coverage':
        print('Coverage not implemented yet.')

    if operation == 'pylint':
        rcfile = project_root / 'dev' / '.pylintrc'
        output = project_root / 'dev' / '.pylint_report'
        cmd = f'pylint kds --rcfile {rcfile} > {output}'
        subprocess.call(cmd, shell=True)

    if operation == 'test':
        print('Tests not implemented yet.')
