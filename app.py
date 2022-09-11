from flask import Flask, render_template, request
from database import database
import json

app = Flask(__name__)
data_base = database()


@app.route("/reach", methods=["POST", "GET"])
def reach():
	return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		password = request.form.get("pass")
		email = request.form.get("email")
		try:
			data_base.auth.sign_in_with_email_and_password(email, password)
			return render_template("index.html")
		except:
			return render_template("login.html")
	else:
		return render_template("login.html")


@app.route('/register', methods =["GET", "POST"])
def register():
	if request.method == "POST":
		first_name = request.form.get("fname")
		last_name = request.form.get("lname")
		password = request.form.get("pass")
		grade = request.form.get("grade")
		email = request.form.get("email")
		try:
			login = data_base.auth.create_user_with_email_and_password(email, password)
			user = data_base.auth.sign_in_with_email_and_password(email, password)

			person = {}
			person["marks"] = ["placeholder"]
			person["fname"] = first_name
			person["lname"] = last_name
			person["grade"] = grade

			data_base.db.child('users').child(user["localId"]).update(person)
			return render_template("index.html")
		except:
			return render_template("login.html")
	return render_template("register.html")


@app.route('/math', methods=["GET", "POST"])
def math():
	data = data_base.db.child("Class1").child("Math").child("Chapter 3").get().val()
	data_dict = {}
	for d in data:
		gif_url = data_base.storage.child("Class1").child("Math").child(f"Chapter3/{data.index(d)}.gif").get_url("asdasdasd")
		d["image"] = gif_url
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