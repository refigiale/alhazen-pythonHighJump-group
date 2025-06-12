import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Machine_learning"

reqget = requests.get(url)


soup = BeautifulSoup(
    reqget.content,
    "html.parser"
)

links = soup.find_all('a')

for link in links:
    print(link.get('href'))