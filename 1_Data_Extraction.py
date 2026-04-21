import requests
from bs4 import BeautifulSoup


bs = BeautifulSoup(requests.get("https://quotes.toscrape.com").text,"html.parser")

# print(bs)


for i in bs.find_all("div",class_="quote"):
    print(i)
    print(i.find("small").text)
    print(i.find("span").text)
    print("------")