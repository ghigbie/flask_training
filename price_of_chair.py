import requests
from bs4 import BeautifulSoup

url = "https://icanhazdadjoke.com"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup)