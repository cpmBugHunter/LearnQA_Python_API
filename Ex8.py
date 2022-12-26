import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"


def _send_get_parameterized(uri, params, delay):
    if delay <= 0:
        resp = requests.get(uri, params=params)
    else:
        time.sleep(delay)
        resp = requests.get(uri, params=params)
    return resp


# Creating task
no_parameter_response = requests.get(url)

try:
    resp_json = no_parameter_response.json()
    token = resp_json['token']
    seconds = resp_json['seconds']
    params = {"token": token}
    print(f"Token is: {token}")
    print(f"Seconds: {seconds}")

    # Send request with parameter before the task completed
    print(f"\nSending second request with parameter token: {token} immediately")

    early_response = _send_get_parameterized(url, params, 0)
    early_json = early_response.json()

    if "status" in early_json:
        if early_json['status'] == "Job is NOT ready":
            print(early_json['status'])
            print("Test result: passed")
        else:
            print(early_json['status'])
            print("Test result: failed")
    else:
        print("Unexpected response returned")

    # Send request with parameter after the task expected to be completed
    print(f"\nSending second request with parameter token: {token} with delay {seconds+1} seconds")
    intime_resp = _send_get_parameterized(url, params, seconds+1)
    intime_json = intime_resp.json()

    if "status" in intime_json and "result" in intime_json:
        if intime_json['status'] == "Job is ready":
            print(f"Status: {intime_json['status']}")
            print(f"Result: {intime_json['result']}")
            print("Test result: passed")
        else:
            print(intime_json['status'])
            print("Test result: failed")
    else:
        print("Unexpected response returned")
except Exception as e:
    print("Something went wrong. Google it using text below: " + str(e))



