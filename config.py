import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgres://kqqosbjxojgacl:11035ded7ad1a400c28f78af1d37b7e054c7362f7ecee3ee55fb596a106f1c17@ec2-18-232-143-90.compute-1.amazonaws.com:5432/d7p5nmq38d18j5'
    print(SQLALCHEMY_DATABASE_URI)
    # 'postgres://kqqosbjxojgacl:11035ded7ad1a400c28f78af1d37b7e054c7362f7ecee3ee55fb596a106f1c17@ec2-18-232-143-90.compute-1.amazonaws.com:5432/d7p5nmq38d18j5'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True