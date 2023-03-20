from app.database.models import User
from app.utils.content import load_menu
from app.utils.content import first_question
from app.api import Wzap

API = Wzap()

def load_data(data:dict):

    full_data:dict = data.get('data')
    phone = full_data.get('fromNumber')
    id_user = full_data.get('chat').get('id')
    name = full_data.get('chat').get('contact').get('displayName')

    if phone =="+5511951414561":return 

    if full_data.get('type') == "text":
        user:User = User.query.filter(User.active==False,
                                    User.phone==phone).first()

        if user and not user.banned:
            menu = load_menu(user.username)
            return API.send_list(phone,menu)
             
        else:
            new:User = User(username=name,chat_id=id_user,
                                phone=phone)
            new.save()

            return API.send_message(phone,first_question)


