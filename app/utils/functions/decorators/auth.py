from flask_jwt_extended import verify_jwt_in_request,get_jwt_identity
from flask import jsonify,request,abort
from functools import wraps
from app import TOKEN


def isAuth(required:bool=False,
            location:str='json'):
    def returnDecorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):

            try:verify_jwt_in_request()
            except:return jsonify({"title":"Sua sessão expirou.","text":"Deslogando..."}),401
            
            user = get_jwt_identity()
            if required:
                if location == "params":kwargs['user_id']=user
                
            return func(*args,**kwargs)

        return wrapper
        
    return returnDecorator  


def isAuthWebhook(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        token = request.args.get("token",None)
        if token and token == TOKEN:
            return func(*args,**kwargs)

        return abort(404)

    return wrapper
        