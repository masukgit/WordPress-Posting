import requests
import base64

api_url = 'https://carcareia.com/wp-json/wp/v2/posts'
username = 'carcareia11'
password = '4SAR R06M D4GU OBLq u7Mt IXPy'

token = base64.b64encode(f'{username}:{password}'.encode()).decode('utf-8')

headers = {
    'Authorization': f'Basic {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
}

data = {
    'title': 'Bob The Marley is the best',
    'content': 'This is a test post created using Python and REST API.',
    'status': 'draft'
}

try:
    res = requests.post(api_url, headers=headers, json=data, timeout=10)
    print('Status:', res.status_code)
    print('Response:', res.text)
except requests.exceptions.RequestException as e:
    print('Error:', e)
