from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup.prettify())

# anchor_tags = soup.find_all("a")
#
# for all_a in anchor_tags:
#     print(all_a.getText())
#     print((all_a.get("href")))

kk = soup.find(class_="heading")
print(kk)
