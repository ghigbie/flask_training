import requests
from bs4 import BeautifulSoup

url = "https://www.johnlewis.com/john-lewis-partners-santino-10-12-seater-extending-dining-table-solid-oak/p3945216"
target_class = "price price--large"
target_id = ""

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find(class_=target_class).get_text().strip()
print(f"The price of the table (not chair) is {element}.")
element2 = soup.select(".price--large")[0].get_text().strip()
print(f"The price of the table (not chair) is {element2}.")

string_price = element[1:]
float_price = float(string_price)
print("##########################################")
if float_price < 1000.00:
    print('You may make this purchase')
else:
    print('You may not make this purchase')