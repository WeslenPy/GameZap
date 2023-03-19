from flask import request,jsonify
from app.utils.functions import authenticate
from app.utils.functions import decorators
from app.blueprints.adm import api_admin_v1



@api_admin_v1.route('/auth',methods=['POST'])
def auth():
   msg = authenticate.login_admin(request.json)
   return jsonify(msg[0]),msg[1]



@api_admin_v1.route("/auth/validate",methods=["GET"])
@decorators.isAuth()
def auth_token():
   return jsonify({"title":"Authorization","text":"ok"}),200
