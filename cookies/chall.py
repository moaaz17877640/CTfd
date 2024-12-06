from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "user" and password == "b4e1c121e5b3676f179e7a2b6541c007579dc7d7":  # base64 10 times the shasum of Us3r_1S_N0t_p0w3rfu11
            return redirect("/home")
        else:
            return "Invalid Username or Password"
    else:
        return render_template("login.html")

@app.route("/home")
def home():
    if request.cookies.get('userID') == 'admin':
        return render_template("flag.html")
    else:
        resp = make_response(render_template('home.html'))
        resp.set_cookie('userID', 'user')
        return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)