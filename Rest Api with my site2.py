import requests
import base64
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

api_url = 'https://carcareia.com/wp-json/wp/v2/posts'

wordpress_user = 'carcareia11'
wordpress_password = '4SAR R06M D4GU OBLq u7Mt IXPy'
credentials = f'{wordpress_user}:{wordpress_password}'
token = base64.b64encode(credentials.encode()).decode('utf-8')

headers = {
    'Authorization': f'Basic {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

data = {
    'title': 'Bob The Marley is the best',
    'content': 'This is a test post created using Python and REST API.',
    'status': 'draft'
}

# Retry strategy
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)

try:
    res = session.post(api_url, headers=headers, json=data, timeout=10)
    print('Status:', res.status_code)
    print('Response:', res.text)
except requests.exceptions.RequestException as e:
    print('Request failed:', e)
