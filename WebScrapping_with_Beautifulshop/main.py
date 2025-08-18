from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# Get all article links
articles = soup.find_all(name='a', class_='storylink')

article_text = []
article_url = []

for article in articles:
    text = article.get_text()
    article_text.append(text)
    url = article.get("href")
    article_url.append(url)

# Get upvotes
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_="score")]

print(article_text)
print(article_url)
print(article_upvote)
max_val=article_upvote.index(max(article_upvote))
print("\n")
print("Print the maximum score of article upvote")
print(f"Article Text : {article_text[max_val]} , With url link : {article_url[max_val]} with total upvotes : {article_upvote[max_val]}")

# for split value of upvote
# no_upvote = []
#
# for i  in range(len(article_upvote)):
#         article_upvote1 = article_upvote[0].split(' ')[0]
#         no_upvote.append(article_upvote1)
# print(no_upvote)
