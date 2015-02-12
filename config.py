import os

PAGE_SIZE = 5

# default config
class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:1qaz@WSX@127.0.0.1:1433/flask'

    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/flask?charset=utf8'

    WEIXIN_TOKEN = 'B0e8alq5ZmMjcnG5gwwLRPW2'

    print SQLALCHEMY_DATABASE_URI


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:1qaz@WSX@127.0.0.1:1433/flask_test'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
