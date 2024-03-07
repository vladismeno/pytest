import requests

from lib.logger import Logger


class MyRequests:

    METHOD_GET = "GET"
    METHOD_POST = "POST"
    METHOD_PUT = "PUT"
    METHOD_DELETE = "DELETE"

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests.__send(url, data, headers, cookies, MyRequests.METHOD_GET)

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests.__send(url, data, headers, cookies, MyRequests.METHOD_POST)

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests.__send(url, data, headers, cookies, MyRequests.METHOD_PUT)

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests.__send(url, data, headers, cookies, MyRequests.METHOD_DELETE)

    @staticmethod
    def __send(url: str, data: dict, headers: dict, cookies: dict, method: str):

        url = f"https://playground.learnqa.ru/api/{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url, data, headers, cookies, method)

        match method:
            case MyRequests.METHOD_GET:
                response = requests.get(url, params=data, headers=headers, cookies=cookies)
            case MyRequests.METHOD_POST:
                response = requests.post(url, params=data, headers=headers, cookies=cookies)
            case MyRequests.METHOD_PUT:
                response = requests.put(url, params=data, headers=headers, cookies=cookies)
            case MyRequests.METHOD_DELETE:
                response = requests.delete(url, params=data, headers=headers, cookies=cookies)
                pass
            case _:
                raise Exception(f"Bad HTTP method '{method}' was received")
                pass

        Logger.add_response(response)

        return response
