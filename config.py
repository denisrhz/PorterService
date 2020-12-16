import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '157da678b99447afbba27733017ee7b9'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://porter:porter51service2001@localhost:3306/porter'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = 'passwwword_salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
