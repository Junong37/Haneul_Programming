import requests
from bs4 import BeautifulSoup

req = requests.get("http://ncov.mohw.go.kr/")
soup = BeautifulSoup(req.content, "html.parser")

div = soup.find("div", class_ = "occur_graph")
table = div.find("table")
td = table.find_all("td")

date_span = soup.find("span", class_ = "livedate")
date = date_span.get_text().split()[0]
div_date = date.split(".")
div_date[0] = div_date[0][1:]

print("{}월 {}일 기준 코로나 신규 확진자: {}".format(div_date[0], div_date[1], td[3].get_text()))