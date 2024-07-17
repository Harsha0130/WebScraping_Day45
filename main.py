from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvote)

largest_upvote = max(article_upvote)
largest_index = article_upvote.index(largest_upvote)

print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_upvote)





















# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
#
# # anchor_tags = soup.find_all("a")
# #
# # for all_a in anchor_tags:
# #     print(all_a.getText())
# #     print((all_a.get("href")))
#
# kk = soup.find(class_="heading")
# print(kk)
