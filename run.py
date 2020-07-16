import os
import pathlib
import subprocess
import sys
import datetime

from kds import create_app

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent
DIR_PACKAGE = PROJECT_ROOT / 'kds'
DIR_PACKAGE_REL = 'kds'
DIR_LANG = DIR_PACKAGE / 'lang'
FIL_BABEL_CFG = DIR_LANG / 'babel.cfg'
FIL_BABEL_POT = DIR_LANG / 'messages.pot'

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

def run_babel(babel_arg):
    if babel_arg == 'extract':
        cmd = ['pybabel', 'extract', '-F', FIL_BABEL_CFG, '-o', FIL_BABEL_POT, DIR_PACKAGE_REL]
    if babel_arg == 'init':
        cmd = ['pybabel', 'init', '-i', FIL_BABEL_POT, '-d', DIR_LANG, '-l', 'de']
    if babel_arg == 'update':
        cmd = ['pybabel', 'update', '-i', FIL_BABEL_POT, '-d', DIR_LANG]
    if babel_arg == 'compile':
        cmd = ['pybabel', 'compile', '-d', DIR_LANG]
    subprocess.call(cmd)
    print('Ran babel.')

if __name__ == '__main__':
    operation = sys.argv[1]
    cmd_args = None
    try:
        cmd_args = sys.argv[2]
    except IndexError:
        pass
    modes = {'app': run_app, 
             'coverage': run_coverage,
             'pylint': run_pylint,
             'test': run_test,
             'babel': run_babel}
    try:
        if cmd_args:
            modes[operation](cmd_args)
        else:
            modes[operation]()
    except KeyError:
        # Display some information when call fails
        print('Usage: run.py [mode]\n')
        print('Available modes are:')
        for mode in modes:
            print(f'* {mode}')
        curr_env = os.environ.get('FLASK_ENV', '[None]')
        print(f'\n$FLASK_ENV is currently set to {curr_env}')
