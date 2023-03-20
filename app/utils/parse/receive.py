from app.utils.content import first_question,reply_message_not_confirm,reply_message_confirm_name
from app.utils.content.button import button_confirm,balance_menu
from app.utils.content import load_menu,load_button
from app.database.models import User
from app.api import Wzap
from app import db

API = Wzap()

def load_data(data:dict):

    full_data:dict = data.get('data')
    phone = full_data.get('fromNumber')
    id_user = full_data.get('chat').get('id')
    name = full_data.get('chat').get('contact').get('displayName')
    body = full_data.get('body')

    type_message = full_data.get('type')
    if phone =="+5511951414561":return 

    user:User = User.query.filter(User.phone==phone).first()
    if type_message == "text":


        if user and not user.banned:
            if user.active:
                menu = load_menu(user.username)
                return API.send_list(phone,menu)
        
            else:
                user.username = body
                db.session.commit()

                buttons = load_button('message',button_confirm,name=body)
                return API.send_button(phone,buttons)
             
        else:
            new:User = User(username=name,chat_id=id_user,
                                phone=phone)
            new.save()

            return API.send_message(phone,first_question)

    elif type_message == "buttons_response":
        id_button = full_data.get('quoted').get('selectedId')
        if id_button=="not_confirm":
            return API.send_message(phone,reply_message_not_confirm)

        elif id_button =="confirm":
            user.active=True
            db.session.commit()
            menu = load_menu(user.username)

            API.send_message(phone,reply_message_confirm_name.format(name=user.username))
            return API.send_list(phone,menu)
        
        elif id_button =="menu_start":
            menu = load_menu(user.username)
            return API.send_list(phone,menu)

    elif type_message == "list_response":
        id_button = full_data.get('quoted').get('selectedId')

        if id_button =="balance":
            balance = f"{user.balance:.2f}".replace(".",",")
            button_balance = load_button('header',balance_menu,name=user.username,balance=balance)
            return API.send_button(phone,button_balance)
        

