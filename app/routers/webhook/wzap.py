from app.blueprints import webhook
from flask import request,jsonify
from app.utils.functions import decorators
from app.utils.parse import load_data
import sys

@webhook.route("/gamezap",methods=["POST","GET"])
@decorators.isAuthWebhook
def webhook_wzap():

    data = request.get_json(force=True,silent=True)
    print(data,file=sys.stderr)

    if data:load_data(data)
    
    return jsonify({"status":200}),200
