from flask import Flask, jsonify

app = Flask(__name__)

courses= [
{
	"userId": 101,
	"id": 0,
	"title": "hello",
	"completed": "false"
},
{
	"userId": 102,
	"id": 1,
	"title": "World",
	"completed": "yes"
},
{
	"userId": 103,
	"id": 2,
	"title": "Welcome",
	"completed": "hmm"
},
{
	"userId": 104,
	"id": 3,
	"title": "Thank you",
	"completed": "ok"
},
{
	"userId": 105,
	"id": 4,
	"title": "Head-ache",
	"completed": "true"
}
]

@app.route("/")
def index():
	return "TEST API"

@app.route("/courses", methods=['GET'])
def get():
	return jsonify({'courses':courses})

@app.route("/courses/<int:id>", methods= ['GET'])
def get_course(id):
	return jsonify({'courses': courses[id]})

@app.route("/courses", methods= ['POST'])
def create():
	course = {
	"userId": 106,
	"id": 5,
	"title": "Go through",
	"completed": "done"}
	courses.append(course)
	return jsonify({'Created': course})

@app.route("/courses/<int:id>", methods= ['PUT'])
def update(id):
	courses[id]['title'] = "Problem Solved"
	return jsonify({'course':courses[id]})

@app.route("/courses/<int:id>", methods= ['DELETE'])
def delete(id):
	courses.remove(courses[id])
	return jsonify({'result': True})


if __name__ == '__main__':
	app.run(debug=True)