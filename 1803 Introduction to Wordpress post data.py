import requests
import base64

api_url = "https://carcareia.com/wp-json/wp/v2/posts"

wordpress_user = "carcareia11"
wordpress_password = "4SAR R06M D4GU OBLq u7Mt IXPy"
wordpress_credential = wordpress_user + ":" + wordpress_password
wordpress_token = base64.b64encode(wordpress_credential.encode())
wordpress_header = {"Authorization" : "Basic " + wordpress_token.decode("utf-8")}

data = {
    "title": "Bob The Marley is the best",
    "content": "While this is about the bob marley, it is true that he is the one who..."
}

res = requests.get(api_url, headers=wordpress_header, json=data) # Add verify=False - if ssl issues
print(res.status_code)