from flask_jwt_extended import verify_jwt_in_request,get_jwt_identity
from flask import jsonify
from functools import wraps

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

