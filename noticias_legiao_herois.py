import requests
from bs4 import BeautifulSoup
from legiao_herois_links import get_posts, array_links

response = requests.get('https://www.legiaodosherois.com.br/?s=anime')
posts = get_posts(response)

links = array_links(posts)

# for link in links:
#   response = requests.get(link)

response_post = requests.get(links[0])
content = response_post.content
site = BeautifulSoup(content, 'html.parser')
content_post = site.find('div', attrs={'class': 'single-post__content post'})
title = content_post.find('h1', attrs={'class': 'post__title bg-ad--disabled'}).text
# subtitle = content_post.find('p', attrs={'class': 'post__tagline'}).text
author = content_post.find('div', attrs={'class': 'post__details__info__feature'}).find('a').text
texts = content_post.find_all('p')
# print(title)
# print(author)

for text in texts:
  print(text.text)

# print(text)