import requests
from bs4 import BeautifulSoup
import pandas as pd
from links_legiao_herois import get_posts, array_links

response = requests.get('https://www.legiaodosherois.com.br/?s=anime')
posts = get_posts(response)

links = array_links(posts)

posts_ready = []

for link in links:
  response_post = requests.get(link)

  content = response_post.content
  site = BeautifulSoup(content, 'html.parser')
  content_post = site.find('div', attrs={'class': 'single-post__content post'})
  
  title = content_post.find('h1', attrs={'class': 'post__title bg-ad--disabled'}).text
  subtitle = content_post.find('p', attrs={'class': 'post__tagline'}).text
  author = content_post.find('div', attrs={'class': 'post__details__info__feature'}).find('a').text
  texts = content_post.find_all('p')

  texts.pop(0)
  texts.pop()

  full_text = []
  for text in texts:
    full_text.append(text.text)

  full_text = " ".join(full_text)

  posts_ready.append([title, subtitle, author, full_text, link])

posts = pd.DataFrame(posts_ready, columns=['Título', 'Subtítulo', 'Author', 'Texto', 'link'])

posts.to_csv('posts_legiao_herois.csv', index=False)