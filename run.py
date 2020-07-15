import os
import pathlib
import subprocess
import sys
import datetime

from kds import create_app

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent

def run_app():
    try:
        env = os.environ['FLASK_ENV']
    except KeyError:
        env = 'development'
        os.environ['FLASK_ENV'] = env
    app = create_app(env)
    app.run()

def run_coverage():
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    output = PROJECT_ROOT / 'dev' / f'coverage_report_{now}'
    htmlcov = PROJECT_ROOT / 'dev' / 'htmlcov'
    os.environ['COVERAGE_FILE'] = str(output)
    cmd = 'coverage run -m unittest discover'
    subprocess.call(cmd, shell=True)
    cmd = f'coverage html -d {htmlcov} --omit="venv/*"'
    subprocess.call(cmd, shell=True)

def run_pylint():
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    rcfile = PROJECT_ROOT / '.pylintrc'
    output = PROJECT_ROOT / 'dev' / f'pylint_report_{now}'
    cmd = f'pylint kds --rcfile {rcfile} > {output}'
    subprocess.call(cmd, shell=True)

def run_test():
    print('Tests not implemented.')

def run_babel():
    cmd = 'pybabel extract -F kds/lang/babel.cfg -o kds/lang/messages.pot kds/'
    cme = 'pybabel init -i kds/lang/messages.pot -d kds/lang -l de'
    cmf = 'pybabel compile -d kds/lang'
    subprocess.call(cmd, shell=True)
    subprocess.call(cme, shell=True)
    subprocess.call(cmf, shell=True)
    print('Ran babel.')

if __name__ == '__main__':
    operation = sys.argv[-1]
    modes = {'app': run_app, 
             'coverage': run_coverage,
             'pylint': run_pylint,
             'test': run_test,
             'babel': run_babel}
    try:
        modes[operation]()
    except KeyError:
        # Display some information when call fails
        print('Usage: run.py [mode]\n')
        print('Available modes are:')
        for mode in modes:
            print(f'* {mode}')
        curr_env = os.environ.get('FLASK_ENV', '[None]')
        print(f'\n$FLASK_ENV is currently set to {curr_env}')
