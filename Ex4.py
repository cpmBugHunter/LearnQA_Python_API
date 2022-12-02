import requests

url = "https://playground.learnqa.ru"
response = requests.get(url + "/api/get_text")
print(response.text)
