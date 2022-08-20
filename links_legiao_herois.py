from bs4 import BeautifulSoup

def get_posts(response):
  content = response.content
  site = BeautifulSoup(content, 'html.parser')
  artigos = site.find('div', attrs={'class': 'articles'})
  posts = artigos.find_all('article', attrs={'class': 'archive__entry'})
  return posts

def array_links(posts):
  links = []
  for post in posts:
    link = post.find('div', attrs={'class': 'archive__entry__details'}).find('a', attrs={'class': 'archive__entry__details__readmore'})
    links.append(link['href'])
  return links
