import requests
from os import environ
import sys
class Wzap:
    def __init__(self) -> None:
        self.token = environ.get('TOKEN')
        self.base_url = "https://api.wzap.chat/v1/{endpoint}"

        self.headers = {
            "Content-Type":"application/json",
            "Token":self.token
        }


    def send_message(self,phone:str,message:str):
        try:

            data = {"phone":phone, "enqueue": "never",'message':message}
            response = requests.post(self.base_url.format(endpoint='messages'),headers=self.headers,json=data)

            if response.status_code == 201:
                return response.json()

            return False

        except Exception as erro:
            return False


    def send_list(self,phone,list_menu):
        try:

            data = {"phone":phone,"list":list_menu}
            response = requests.post(self.base_url.format(endpoint='messages'),headers=self.headers,json=data)


            print(response.json(),file=sys.stderr)
            if response.status_code == 201:
                return response.json()

            return False

        except Exception as erro:
            return False

