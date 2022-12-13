import requests

url = "https://playground.learnqa.ru"
urls = []
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/107.0.0.0 Safari/537.36 "
headers = {"user-agent": user_agent}

try:
    response = requests.get(f"{url}/api/long_redirect", headers=headers)
    history = response.history

    for i in history:
        urls.append(i.url)

    redirects_count = len(urls) - 1 #Because the first URL was the requested one. It is also a number of the last URL

    print(response.status_code)
    print(f"Redirects count: {redirects_count}")
    print(f"The last URL was: {urls[redirects_count]}")
except Exception as e:
    print("Something went wrong. Google it using text below: " + str(e))

