import requests

url = 'https://carcareia.com/wp-json/wp/v2/posts'
res = requests.get(url)
if res.status_code == 200:
    data =res.json()
    for post in data:
        print(post.get('link'))
