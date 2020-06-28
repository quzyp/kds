""" The default configuration, aimed at development. The production
configuration goes in $root/instance/config.py """

class Config:
    """ Basic configuration. """

    TESTING = False
    DEBUG = False
    ENVIRON = 'None'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigDev(Config):
    """ The development configuration. Uses an in-memory
    database and debugging. """

    DEBUG = True
    ENVIRON = 'development'
    SQLALCHEMY_ECHO = True
    ASSETS_DEBUG = True
    SECRET_KEY = 'shush'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

    print('#################################')
    print('RUNNING FLASK IN DEVELOPMENT MODE')
    print('#################################')
