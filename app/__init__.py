from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app,db)
jwt = JWTManager(app)

token_s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

TOKEN =  app.config["TOKEN"]
PER_PAGE=15

from .database import *
from .routers import *

from .blueprints import *


app.register_blueprint(blueprint=api_admin_v1)
app.register_blueprint(blueprint=dash_admin)
app.register_blueprint(blueprint=webhook)


