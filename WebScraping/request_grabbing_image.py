import bs4
import requests

request = requests.get("https://en.wikipedia.org/wiki/Captains_of_the_Sands")
soup = bs4.BeautifulSoup(request.text, "lxml")
book = soup.select("img")[0]
print(f"1: {book}")
print(f"2: {type(book)}")
src_image = "https:"+book['src']
print(f"3: {src_image}")
image_link = requests.get(src_image)
f = open("book_image.jpg", "wb")
f.write(image_link.content)
f.close()
