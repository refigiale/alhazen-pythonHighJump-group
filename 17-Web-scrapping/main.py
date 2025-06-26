import requests

url = "https://en.wikipedia.org/wiki/Machine_learning"

reqget = requests.get(url)


with open("index.html", "w", encoding="utf-8") as f:
    f.write(reqget.text)