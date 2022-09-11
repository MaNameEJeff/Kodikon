from flask import Flask, render_template, request
from database import database
import json

app = Flask(__name__)
data_base = database()


@app.route("/reach", methods=["POST", "GET"])
def reach():
	return render_template("index.html")

def chapter(ch_no):
	global chapter_number
	with open("./static/js/chapter.json", "r") as file:
		data = json.load(f)
		chapter_number = data["ch_no"]


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		password = request.form.get("pass")
		email = request.form.get("email")
		try:
			global user
			user = data_base.auth.sign_in_with_email_and_password(email, password)
			json_object = json.dumps({"userName": dict(data_base.db.child("users").child(user["localId"]).get().val())["fname"]})
			with open("./static/js/user.json", "w") as file:
				file.write(json_object)
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
			global user
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
	global chapter_number
	global user
	chapter_number = 3
	user_grade = dict(data_base.db.child("users").child(user["localId"]).get().val())["grade"][1]
	data = data_base.db.child(f"Class{user_grade}").child("Math").child(f"Chapter {chapter_number}").get().val()
	data_dict = {}
	for d in data:
		gif_url = data_base.storage.child(f"Class{user_grade}").child("Math").child(f"Chapter{chapter_number}/{data.index(d)}.gif").get_url("asdasdasd")
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