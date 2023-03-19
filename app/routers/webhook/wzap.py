from app.blueprints import webhook
from flask import request,jsonify
from app.utils.functions import decorators
import sys

@webhook.route("/gamezap",methods=["POST","GET"])
@decorators.isAuthWebhook
def webhook_wzap():

    print(request.get_json(force=True,silent=True),file=sys.stdout)
    
    return jsonify({"status":200}),200

