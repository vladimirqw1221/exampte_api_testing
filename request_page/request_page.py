from utilites.http_requesrs import HttpMethodsClass
from base_class.base_class import BaseClass
from cofiguretions import BASE_URL
from dicts.headers_value import DictsClas
from dotenv import load_dotenv
import os


class RequestClass(BaseClass):
    title_value = DictsClas()
    load_dotenv()

    def __init__(self):
        super().__init__()

    def create_token_auth(self):
        patch = "/auth"
        data = {"username": os.getenv('UNAME'),
                "password": os.getenv('PAWORD')}

        response = HttpMethodsClass.post_requests(BASE_URL + patch, data)
        self.checking_json_value(response, 200, self.title_value.TOKEN)
        return response

    def gitting_books(self):
        patch = "/booking"
        response = HttpMethodsClass.get_requests(BASE_URL + patch)
        self.checking_status_code_and_title_in_request(response, 200, self.title_value.BOOKINGID)
        return response

    def gitting_books_id(self):
        patch = "/booking/1"
        response = HttpMethodsClass.get_requests(BASE_URL + patch)
        self.checking_status_code_and_title_in_request(response, 200, self.title_value.FIRSTNAME)
        return response

    def create_books(self):
        patch = "/booking"
        data = {
            "firstname": "Test",
            "lastname": "Test",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Test"
        }
        response = HttpMethodsClass.post_requests(BASE_URL + patch, data)
        self.checking_status_code_and_title_in_request(response, 200, self.title_value.FIRSTNAME)

    def update_books_info(self):
        patch = "/booking/1"
        data = {
            "firstname": "Test",
            "lastname": "Test",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Update"
        }
        response = HttpMethodsClass.put_requests(BASE_URL + patch, data)
        self.checking_status_code_and_title_in_request(response, 200, self.title_value.FIRSTNAME)

        return response

    def updata_first_name(self):
        patch = "/booking/1"
        data = {
            "firstname": "Test",
            "lastname": "Brown"
        }
        response = HttpMethodsClass.patch_requests(BASE_URL + patch, data)

        self.checking_json_value(response, 200, self.title_value.FIRSTNAME)
        return response


    def delete_first_name(self):
        patch = "/booking/1"
        data = {}

        response = HttpMethodsClass.delete_requests(BASE_URL + patch, data)

        self.checking_status_code_and_title_in_request(response, 201, self.title_value.CREATED)
        return response

    def ping_shop(self):
        patch = "/ping"
        response = HttpMethodsClass.get_requests(BASE_URL + patch)
        self.checking_status_code_and_title_in_request(response, 201, self.title_value.CREATED)
        return response
