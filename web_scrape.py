import requests
url = "https://icanhazdadjoke.com/"

request = requests.get(url)
print(request.content)