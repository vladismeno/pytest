from json.decoder import JSONDecodeError

import requests

# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])

# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not JSON format")



# response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/something")
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# response1 = response.history[0]
# response2 = response
# print(response1.url + ":" + str(response1.status_code))
# print(response2.url + ":" + str(response2.status_code))


# headers = {"some_header": "123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
# print(response.text)
# print(response.headers)


# payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# cookie_value = response1.cookies.get('auth_cookie')
# cookies = {}
# if cookie_value is not None:
#     cookies.update({'auth_cookie': cookie_value})
#
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
#
# print(response2.text)