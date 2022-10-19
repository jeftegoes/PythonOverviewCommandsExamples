import bs4
import requests

request = requests.get("https://pt.wikipedia.org/wiki/Jorge_Amado")
soup = bs4.BeautifulSoup(request.text, "lxml")
first_item = soup.select('.sidebar-toc-text')[0]
print(f"1: {soup}")
print(f"2: {first_item}")
print(f"3: {first_item.text}")
for item in soup.select('.sidebar-toc-text'):
    text = item.text.replace('\n', '')
    print(f"4: {text}")
