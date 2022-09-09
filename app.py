from flask import Flask, render_template

app = Flask(__name__)

@app.route("/reach", methods=["GET"])
def reach():
	return render_template("index.html")

@app.route("/test", methods=["GET"])
def test():
	return render_template("charts.html")

if __name__ == '__main__':
	app.run(debug=True)