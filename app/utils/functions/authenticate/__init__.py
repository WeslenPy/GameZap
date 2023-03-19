from app.utils.functions.crypt import decryptPassword
from app.database.models import AdminPainel
from flask_jwt_extended import create_access_token
from flask import session
from datetime import timedelta


def login_admin(data:dict):
    email = data.get('email','')
    password = data.get('password','')

    admin:AdminPainel = AdminPainel.query.filter_by(email=email).first()

    if admin:
        if decryptPassword(password,admin.password):
            token = create_access_token(identity=admin.id,expires_delta=timedelta(days=1))

            session['admin_logger'] = [token,True]

            return {'message':{"title":"Login","text":"Login efetuado com sucesso.","icon":"success"},'access_token':token},200

    return {'text':'Email ou senha incorretos',"title":"Oops, revise os dados.",'error':1},400