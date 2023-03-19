import requests
from os import environ

class Wzap:
    def __init__(self) -> None:
        self.token = environ.get('TOKEN')
        self.base_url = "https://api.wzap.chat/v1/{endpoint}"

        self.headers = {
            "Content-Type":"application/json",
            "Token":self.token
        }


    def send_message(self,phone,message):
        try:

            data = {"phone":phone,'message':message}
            response = requests.post(self.base_url.format(endpoint='messages'),headers=self.headers,json=data)

            if response.status_code == 201:
                return response.json()

            return False

        except Exception as erro:
            return False


    def send_list(self,phone,title,list):
        try:

            # data = {"phone":phone,'message':message}
            response = requests.post(self.base_url.format(endpoint='messages'),headers=self.headers,json=data)

            if response.status_code == 201:
                return response.json()

            return False

        except Exception as erro:
            return False

api = Wzap()

ls = api.send_message('+559885653456','Olá')
print(ls)