import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ''' Parent Configuration '''
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

class Development(Config):
    ''' Configuration for development '''
    DEBUG = True
    CORS_ENABLED = True

class Testing(Config):
    TESTING = True
    DEBUG = True

class Staging(Config):
    DEBUG = True

class Production(Config):
    DEBUG = False   
    TESTING = False

app_config = {
    'development': Development,
    'testing' : Testing,
    'staging' : Staging,
    'production' : Production
}

