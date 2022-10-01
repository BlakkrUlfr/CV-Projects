from bs4 import BeautifulSoup

import requests

response = requests.get(url='https://news.ycombinator.com/news?p=2')

yc_web_page = response.text

soup = BeautifulSoup(markup=yc_web_page, features='html.parser')

# a_tag = soup.select_one(selector='.titlelink')
# print(type(a_tag))
# article_text = a_tag.get_text()
# print(article_text)

# article_link = a_tag.get(key='href')
# print(article_link)

# span_tag = soup.select_one(selector='.score')
# article_upvote_text = span_tag.getText()
# print(article_upvote_text)

all_a_tags = soup.find_all(name='a', class_='titlelink')
# print(all_a_tags)

article_texts_a = []
article_links_a = []

for atag in all_a_tags:
    a_link = atag.get(key='href')
    article_links_a.append(a_link)
    a_text = atag.get_text()
    article_texts_a.append(a_text)

all_span_tags = soup.find_all(name='span', class_='score')
# print(all_span_tags)
span_score_texts = [spantag.getText() for spantag in soup.find_all(name='span', class_='score')]
# span_score_texts = [span_tag.getText() for span_tag in all_span_tags]
# print(span_score_texts)

article_span_score_int = [int(spantag.getText().split()[0]) for spantag in soup.find_all(name='span', class_='score')]
# span_score_int = [int(spantag_string.split()[0]) for spantag_string in span_score_texts]
print(article_span_score_int)

print(article_texts_a)
print(article_links_a)

most_article_upvotes = max(article_span_score_int)

largest_index = article_span_score_int.index(most_article_upvotes)

# the_index = 0
# highest = article_span_score_int[0]

# for index in range(1, len(article_span_score_int)):
#     if highest < article_span_score_int[index]:
#         the_index = index
#         highest = article_span_score_int[index]

print(article_links_a[largest_index])
print(article_texts_a[largest_index])