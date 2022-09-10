from flask import Flask, render_template
import json

app = Flask(_name_)
data_base = database()

@app.route("/reach", methods=["GET"])
def reach():
	return render_template("index.html")

@app.route('/math', methods=["GET", "POST"])
def math():
	data = data_base.db.child("Class1").child("Math").child("Chapter 1").get().val()
	data_dict = {}
	for d in data:
		data_dict[data.index(d)] = d;
	json_object = json.dumps(data_dict, indent=4)
	with open("./static/js/questions.json", "w") as file:
		file.write(json_object)
	return render_template("interactive_math.html")

@app.route("/test", methods=["GET"])
def test():
	return render_template("test.html")

if _name_ == '_main_':
	app.run(debug=True)