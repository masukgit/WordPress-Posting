from requests import post
import base64
api_url = 'https://carcareia.com/wp-json/wp/v2/posts'

wordpress_user = 'carcareia11'
wordpress_pass = '4SAR R06M D4GU OBLq u7Mt IXPy'
token = base64.b64encode(f'{wordpress_user} : {wordpress_pass}'.encode()).decode('utf-8')
headers = {
    'Authorization': f'Basic {token}',
    'User-Agent': 'Firefox/5.0'
}
content = '<!-- wp:paragraph --><p>Mr. Younus is rejected to meet by Mr. Kiar Starmar, the prime minister of the people republic of England</p><!-- /wp:paragraph -->'
data = {
    'title': 'Kiar Starmar is the player',
    'categories': '9',
    'slug': 'kiar-starmar-the-player',
    'content': content,
    'status': 'draft'
}

res = post(api_url, headers=headers, json=data)
print(res.status_code)
