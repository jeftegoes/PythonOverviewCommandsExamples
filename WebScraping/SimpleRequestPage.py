import bs4
import requests

request = requests.get("http://example.com/")
soup = bs4.BeautifulSoup(request.text, "lxml")
print(f"1: {type(request)}")
print(f"2: {request.text}")
print(f"3: {soup.select('title')[0].getText()}")
print(f"4: {soup.select('p')[0].getText()}")
