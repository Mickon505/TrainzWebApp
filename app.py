from flask import Flask, render_template, request, redirect, url_for, session
import Database
import time
import threading

fireDB = Database.Firebase()
mongoDB = Database.Mongo("mongodb+srv://thejacob:Komjatice0258@trainz.tverj.mongodb.net/trainzDB?retryWrites=true&w=majority",
						"trainzDB", "trainzCOL")

app = Flask(__name__)
app.config["SECRET_KEY"] = "bababoiLoves3DPrints"
app.config["SESSION_PERMANENT"] = True
app.config["TEMPLATE_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def home():
	session["s"] = True
	if not session.get("logged"):
		return render_template("login.html", err=None)

	else:
		return redirect("/control")


@app.route("/control", methods=["POST", "GET"])
def controller():
	if fireDB.get_data("track_status", "track01") > 0:
		return redirect("/waitingroom")

	return render_template('controller.html')


@app.route("/start", methods=["POST", "GET"])
def start_train():
	if request.method == "GET":
		return redirect("https://youtu.be/dQw4w9WgXcQ")

	if request.method == "POST":
		print("[Train] Status: Moving forward (axis: 1)")
		fireDB.update_data({"axis": 1}, "trainz01")
		return "train started"


@app.route("/stop", methods=["POST", "GET"])
def stop_train():
	if request.method == "GET":
		return redirect("https://youtu.be/dQw4w9WgXcQ")

	if request.method == "POST":
		print("[Train] Status: Idling (axis: 0)")
		fireDB.update_data({"axis": 0}, "trainz01")
		return "train stopped"


@app.route("/rev", methods=["POST", "GET"])
def reverse():
	if request.method == "GET":
		return redirect("https://youtu.be/dQw4w9WgXcQ")

	if request.method == "POST":
		print("[Train] Status: Moving back (axis: -1)")
		fireDB.update_data({"axis": -1}, "trainz01")
		return "train reversed"


@app.route("/rr", methods=["POST"])
def switch_rail_road():
	if request.method == "GET":
		return redirect("https://youtu.be/dQw4w9WgXcQ")

	if request.method == "POST":
		print("[Rail Road] Switch set to:", request.form.get("signal"))

		rrSwitch = True if request.form.get("signal") == "true" else False

		fireDB.update_data({"rail_switch": rrSwitch}, "track01")
		return ""


@app.route("/login", methods=["POST", "GET"])
def login():
	err = None
	session["s"] = True
	if request.method == "POST":

		if mongoDB.get({request.form.get("user"): request.form.get("pw")}):
			session["logged"] = True

			return redirect("/logged")

		else:
			err = "Wrong username or password"
			return render_template("login.html", error=err)


@app.route("/logged")
def logged():
	return render_template("login.html", err=None)


@app.route("/instructions")
def info():
	return render_template("info.html")


@app.route("/waitingroom")
def wr():
	return render_template("waiting_room.html")


@app.route("/thanks_for_playing")
def thx4playing():
	return render_template("thanks4playing.html")


@app.route("/startengine", methods=["POST"])
def start_engine():
	if request.method == "POST":
		engine = True if request.form.get("signal") == "true" else False

		if not engine:
			fireDB.update_data({"track_status": 0}, "track01")
			session["engine"] = False
			return redirect("thanks_for_playing")

		elif fireDB.get_data("track_status", "track01") > 0:
			return redirect("/waitingroom")

		elif fireDB.get_data("track_status", "track01") == 0 and engine:
			session["engine"] = True
			fireDB.update_data({"track_status": 1}, "track01")
			return ""


if __name__ == '__main__':
	app.run(debug=True)
