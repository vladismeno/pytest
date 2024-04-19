from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests



class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_data = {
            "username": "New User Name",
            "firstName": "New First Name",
            "lastName": "New Last Name",
            "email": self.generate_email()
        }

        response3 = MyRequests.put(
            f"user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data=new_data
        )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        actual_data = response4.json()
        for key, value in new_data.items():
            Assertions.assert_json_value_by_key(
                response4,
                key,
                value,
                f"Wrong {key} after edit. Expected: {value}, Actual: {actual_data[key]}"
            )
