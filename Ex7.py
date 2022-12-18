import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
query_types = ["GET", "POST", "PUT", "DELETE", "HEAD", "CONNECT", "OPTIONS", "TRACE", "PATCH"]

no_param_response = requests.get(url)
print(no_param_response.text)

responses = []
for qt in query_types:
    for p in query_types:
        if qt == "GET":
            param = p
            params = {"method": param}
            resp = requests.request(qt, url, params=params)
        elif qt in ("POST", "PUT", "PATCH"):
            param = p
            payloads = {"method": param}
            resp = requests.request(qt, url, data=payloads)
        else:
            param = f"{p} was not sent"
            resp = requests.request(qt, url)

        method_type_response = dict(method=qt, parameter=param, response=resp.text)
        print(method_type_response)
        responses.append(method_type_response)

incorrect_responses = []
for r in responses:
    method = r["method"]
    parameter = r["parameter"]
    response = r["response"]
    if method == parameter:
        if not response.lower().__contains__("success"):
            incorrect_responses.append(r)
    else:
        if response.lower().__contains__("success"):
            incorrect_responses.append(r)
print("\n Incorrect responses are: \n")
for u in incorrect_responses:
    print(u)
