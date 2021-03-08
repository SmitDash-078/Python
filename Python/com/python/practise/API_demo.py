import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
print(resp.text)