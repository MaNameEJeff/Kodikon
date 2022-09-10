from flask import Flask, render_template

app = Flask(__name__)

@app.route("/reach", methods=["GET"])
def reach():
	return render_template("index.html")

@app.route("/test", methods=["GET"])
def test():
	return render_template("charts.html")
@app.route('/math', methods=["GET", "POST"])
def my_link():
	data = data_base.db.child("Class2").child("Math").child("Chapter 1").get().val()
	data_dict = {}
	for d in data:
		data_dict[data.index(d)] = d;
	json_object = json.dumps(data_dict, indent=4)
	with open("./static/js/questions.json", "w") as file:
		file.write(json_object)
	return "Clicked"

if __name__ == '__main__':
	app.run(debug=True)