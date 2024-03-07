from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    def test_create_user_with_existing_email(self):
        data = self.prepare_registration_data("vinkotov@example.com")

        response = MyRequests.post("user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{data['email']}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
