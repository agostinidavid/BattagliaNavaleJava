from flask import Flask, url_for, redirect, render_template, request, g
from flask_login import login_user, current_user, LoginManager, logout_user
from lib.__database__ import getUser, checkUser, createUser
from lib.__user__ import User
import datetime

app = Flask(__name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    for i in ["(",")"," ", "'"]:
        user_id = user_id.replace(i,'')
    user_id = user_id.split(',')
    id, name, lastName, email = user_id
    return User(id=id, name=name, lastName=lastName, email=email)

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template("home.html")
    return redirect(url_for("login"))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/registerForm", methods=['POST'])
def registerForm():
    name = request.form["nameInput"]
    lastName = request.form["lastNameInput"]
    email = request.form["emailInput"]
    password = request.form["passwordInput"]
    createUser(name=name, lastName=lastName, email=email, password=password)
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginForm", methods=['POST'])
def loginForm():
    if checkUser(request.form["emailInput"], request.form["passwordInput"]):
        user = User(getUser(request.form["emailInput"]))
        login_user(user)
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__": 
    login_manager.login_view = 'app.login'
    login_manager.session_protection = 'strong'  
    login_manager.init_app(app)
    app.secret_key= "oyievqgeaeqwedgcbkulusehdfewkb"
    app.run(
        host="0.0.0.0", 
        port=5000, 
        use_reloader=True, 
        debug=True)
    