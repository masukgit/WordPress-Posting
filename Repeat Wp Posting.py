import requests
import base64

api_url = 'https://carcareia.com/wp-json/wp/v2/posts'

wordpress_user = 'carcareia11'
wordpress_pass = '4SAR R06M D4GU OBLq u7Mt IXPy'
wordpress_credential = wordpress_user + ':' + wordpress_pass
wordpress_token = base64.b64encode(wordpress_credential.encode()).decode('utf-8')
wp_headers = {
    'Authorization': f'Basic {wordpress_token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

data = {
    'title': 'Trump is a poor guy',
    'content': 'This is a test post created using Python and REST API about Trump.',
    'status': 'draft'
}
res = requests.post(api_url, headers=wp_headers, json=data, timeout=10)
print('Status:', res.status_code)
print('Response:', res.text)