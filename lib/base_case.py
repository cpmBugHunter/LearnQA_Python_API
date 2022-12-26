import json.decoder

from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can not find cookie '{cookie_name}' in the last response"
        return response.cookies[cookie_name]


    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Can not find header '{header_name}' in the last response"
        return response.headers[header_name]


    def get_json_value(self, response: Response, key):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert key in response_as_dict, f"Response JSON doesn't have key '{key}'"

        return response_as_dict[key]
