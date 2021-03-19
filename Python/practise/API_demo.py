from flask import Flask,jsonify
import requests

app= Flask(__name__)

# fetch('https://jsonplaceholder.typicode.com/todos/1')
#   .then(response => response.json())
#   .then(json => console.log(json))

def get():
	resp= requests.get("https://jsonplaceholder.typicode.com/todos/1")
	return jsonify({"Couses":resp.text})