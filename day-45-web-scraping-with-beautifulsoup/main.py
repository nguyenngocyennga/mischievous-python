from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
article_texts = []
article_links = []
article_upvotes = []

articles = soup.find_all(name="a", class_="storylink")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    next_element = article_tag.parent.parent.next_sibling.contents[1].contents[1].string
    has_score = next_element.split()[1] == "points"
    if has_score:
        score = int(next_element.split()[0])
        article_upvotes.append(score)
    else:
        article_upvotes.append(0)

largest_number = max(article_upvotes)
index = article_upvotes.index(largest_number)

print(article_texts[index])
print(article_links[index])
# print(article_upvotes[index])
# print(article_upvotes)
# print(len(article_upvotes))
