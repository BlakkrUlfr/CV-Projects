import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(markup=website_html, features='html.parser')
# print(soup.prettify())

all_movies_h3 = soup.find_all(name='h3', class_='title')

movie_titles_h3 = [movie_h3.getText() for movie_h3 in all_movies_h3]

print(movie_titles_h3)

reversed_list = movie_titles_h3[::-1]

# for n in range(len(movie_titles_h3) - 1, -1, -1):
#     print(movie_titles_h3[n])

print(reversed_list)

with open(file='movies.txt', mode='w', encoding='utf-8') as file:
    for movie_title_h3 in reversed_list:
        file.write(f'{movie_title_h3}\n')