import requests
from legiao_herois_links import get_posts, array_links

response = requests.get('https://www.legiaodosherois.com.br/?s=anime')
posts = get_posts(response)

print(array_links(posts))