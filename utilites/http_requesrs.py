import requests
from base_class.base_class import BaseClass
from utilites.logger import Logger


class HttpMethodsClass(BaseClass):

    def __init__(self):
        super().__init__()

    headers = {'Content-Type': 'application/json',
               }
    cookie = BaseClass()
    get_cookie = cookie.get_cookie()

    @staticmethod
    def get_requests(url):
        """This method for launch getting requests
        Logger gitignore """
        # Logger.request_logs(url=url, method="GET")
        response = requests.get(url=url, headers=HttpMethodsClass.headers, cookies=HttpMethodsClass.get_cookie)
        # Logger.response_logs(response=response)
        return response

    @staticmethod
    def post_requests(url, body):
        """This method for launch post requests
        Logger gitignore"""
        # Logger.request_logs(url=url, method="Post")
        response = requests.post(url=url, headers=HttpMethodsClass.headers, cookies=HttpMethodsClass.get_cookie,
                                 json=body)
        # Logger.response_logs(response=response)
        return response

    @staticmethod
    def put_requests(url, body):
        """This method for launch put requests
        Logger gitignore"""
        # Logger.request_logs(url=url, method="Post")
        response = requests.put(url=url, headers=HttpMethodsClass.headers, cookies=HttpMethodsClass.get_cookie,
                                json=body)
        # Logger.response_logs(response=response)
        return response

    @staticmethod
    def delete_requests(url, body):
        # Logger.request_logs(url=url, method="Post")
        """This method for launch delete requests
        Logger gitignore"""
        response = requests.delete(url=url, headers=HttpMethodsClass.headers, cookies=HttpMethodsClass.get_cookie,
                                   json=body)
        # Logger.response_logs(response=response)
        return response

    @staticmethod
    def patch_requests(url, body):
        """This method for launch patch requests
        Logger gitignore"""
        # Logger.request_logs(url=url, method="Post")
        response = requests.patch(url=url, headers=HttpMethodsClass.headers, cookies=HttpMethodsClass.get_cookie,
                                  json=body)
        # Logger.response_logs(response=response)
        return response
