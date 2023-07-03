from requests import Response
from src.enums.global_enums import GlobalEnumsClass
import requests
import os
from dotenv import load_dotenv




class BaseClass:
    load_dotenv()

    def __init__(self):
        pass


    def get_cookie(self):
        data = {"username": os.getenv('UNAME'),
                "password": os.getenv('PAWORD')}
        get_cokkie = requests.post("https://restful-booker.herokuapp.com/auth", data=data)
        gitting_cookies = get_cokkie.json()
        return gitting_cookies


    def checking_status_code_and_title_in_request(self, response: Response, status_code, title_value):
        """This method for checking title for get request"""
        if response.status_code == status_code:
            print(f"\nStatus code valid {response.status_code}")
            if title_value in response.text:
                print("Test headers passed")
            else:
                print("Test headers Fail")
                assert False, GlobalEnumsClass.WRONG_TITLE.value
        else:
            print(f"Status code in not 200, status code your requests: {response.status_code}")
            assert False, GlobalEnumsClass.WRONR_STATUS_CODE.value

    def checking_json_value(self, response: Response, status_code, json_value):
        """This method for checking json for post request"""
        assert response.status_code == status_code, GlobalEnumsClass.WRONR_STATUS_CODE.value
        print(f"\nStatus code : {response.status_code}")
        assert json_value in response.json(), GlobalEnumsClass.WRONG_TITLE.value
        print(f"JSON value: {response.json()}")
