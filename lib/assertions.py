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