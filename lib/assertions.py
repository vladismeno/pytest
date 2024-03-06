from requests import Response
import json
class Assertions:
    @staticmethod
    def assert_json_value_by_key(response: Response, key, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert key in response_as_dict, f"Response JSON doesn't have a key '{key}'"
        assert response_as_dict[key] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, key):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert key in response_as_dict, f"Response JSON doesn't have a key '{key}'"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code!  Expected: {expected_status_code}. Actual: {response.status_code}"

