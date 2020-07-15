""" The default configuration, aimed at development. The production
configuration goes in $root/instance/config.py """

import pathlib

class Config:
    """ Basic configuration. """

    TESTING = False
    DEBUG = False
    ENVIRON = 'None'
    DIR_ROOT = pathlib.Path(__file__).resolve().parent.parent
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_TRANSLATION_DIRECTORIES = str(DIR_ROOT / 'kds' / 'lang')

class ConfigDev(Config):
    """ The development configuration. Uses an in-memory
    database and debugging. """

    DEBUG = True
    ENVIRON = 'development'
    #SQLALCHEMY_ECHO = True
    #ASSETS_DEBUG = True
    SECRET_KEY = 'shush'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

    print('#################################')
    print('RUNNING FLASK IN DEVELOPMENT MODE')
    print('#################################')
