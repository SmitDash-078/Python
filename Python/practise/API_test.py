import requests

created=[
    {"userId": 106,
	"id": 5,
	"title": "Go through",
	"completed": "done"}
]

resp=requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(resp.text)
