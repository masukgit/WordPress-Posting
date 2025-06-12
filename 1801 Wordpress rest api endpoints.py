import requests

route = 'https://themeisle.com/wp-json/'

res = requests.get(route)

if res.status_code == 200:
    data = res.json()
    site_name = data.get('name')
    site_url = data.get('url')
    print(site_name, site_url, sep=', ')


