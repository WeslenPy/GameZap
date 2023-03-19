from flask import Blueprint

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')