import requests
from bs4 import BeautifulSoup

url = "https://www.johnlewis.com/john-lewis-partners-santino-10-12-seater-extending-dining-table-solid-oak/p3945216"
target_class = "price price--large"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find_all("p", {"class" : target_class} )
print(f"The price of the table (not chair is {element.text}")

