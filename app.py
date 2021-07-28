from flask import Flask, render_template, request, redirect, url_for, session
from Database import Firebase

fireDB = Firebase()
app = Flask(__name__)
app.config["SECRET_KEY"] = "bababoiLoves3DPrints"
app.config["SESSION_PERMANENT"] = True
app.config["TEMPLATE_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def home():
	if not session.get("logged"):
		return render_template("login.html", err=None)

	else:
		return render_template("controller.html")


@app.route("/control", methods=["POST", "GET"])
def controller():
	return render_template('controller.html')


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


@app.route("/rr", methods=["POST"])
def switch_rail_road():
	if request.method == "POST":
		print(request.form.get("signal"))
		fireDB.push_data({"rail_switch": True}, "track01")
		return ""


@app.route("/login", methods=["POST", "GET"])
def login():
	err = None

	if request.method == "POST":

		if request.form.get("user") == "admin" and request.form.get("pw") == "admin1":
			print("Create session")
			session["logged"] = True
			return redirect("/logged")

		else:
			err = "Wrong username or password"
			return render_template("login.html", error=err)


@app.route("/logged")
def logged():
	return render_template("login.html", err=None)


if __name__ == '__main__':
	app.run(debug=True)
