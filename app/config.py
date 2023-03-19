from dotenv import load_dotenv
load_dotenv()

from os import environ
from datetime import timedelta


# secret key para as sessões
SECRET_KEY = environ.get('SECRET_KEY','secret-fuerte')

# SQLALCHEMY CONFIGS
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI','')
SQLALCHEMY_POOL_RECYCLE= int(environ.get('SQLALCHEMY_POOL_RECYCLE',299))
SQLALCHEMY_POOL_TIMEOUT= int(environ.get('SQLALCHEMY_POOL_TIMEOUT',20))
SQLALCHEMY_POOL_SIZE= int(environ.get('SQLALCHEMY_POOL_SIZE',10000))
SQLALCHEMY_MAX_OVERFLOW= int(environ.get('SQLALCHEMY_MAX_OVERFLOW',500))
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY","super-secret")
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)
JWT_TOKEN_LOCATION = ['headers']
JWT_HEADER_NAME = "Authorization"
JWT_HEADER_TYPE = "Bearer"

# CONFIGURAÇÕES DO JSON PARA UTF-8
JSON_AS_ASCII = False
JSONIFY_PRETTYPRINT_REGULAR = True

MAX_CONTENT_LENGTH = 5048

TESTING = False
