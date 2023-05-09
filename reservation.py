import requests
from bs4 import BeautifulSoup

url = "https://songdotennis.co.kr/reservation"

response = requests.get(url)

print(response)
print(response.text)
