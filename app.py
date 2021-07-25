from flask import Flask, render_template, request
from Database import Firebase

fireDB = Firebase()
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "POST":
		signal = request.form.keys()
		print(signal)

	return render_template('index.html')


@app.route("/start", methods=["POST", "GET"])
def start_train():
	if request.method == "POST":
		fireDB.push_data({"axis": 1}, "trainz01")
		return "train started"


@app.route("/stop", methods=["POST", "GET"])
def stop_train():
	if request.method == "POST":
		fireDB.push_data({"axis": 0}, "trainz01")
		return "train stopped"


@app.route("/rev", methods=["POST", "GET"])
def reverse():
	if request.method == "POST":
		fireDB.push_data({"axis": -1}, "trainz01")
		return "train reversed"


if __name__ == '__main__':
	app.run(host="192.168.0.20", port=5000)
