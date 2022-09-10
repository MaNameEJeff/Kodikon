from flask import Flask, render_template
from database import database
import json

app = Flask(__name__)
data_base = database()


@app.route("/reach", methods=["GET"])
def reach():
	return render_template("index.html")


@app.route("/login", methods=["GET"])
def login():
	return render_template("login.html")


@app.route("/register", methods=["GET"])
def register():
	return render_template("register.html")


@app.route('/math', methods=["GET", "POST"])
def math():
	data = data_base.db.child("Class1").child("Math").child("Chapter 1").get().val()
	data_dict = {}
	for d in data:
		data_dict[data.index(d)] = d
	json_object = json.dumps(data_dict, indent=4)
	with open("./static/js/questions.json", "w") as file:
		file.write(json_object)
	return render_template("interactive_math.html")


@app.route("/test", methods=["GET"])
def test():
	return render_template("test.html")


if __name__ == '__main__':
	app.run(debug=True)
	# data_base = database()
	# t = data_base.storage.child("Class1").child("Math").child("Chapter3/4.gif").get_url("sdfds")
	# print(t)