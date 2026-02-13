from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager, UserMixin,
    login_user, logout_user,
    login_required, current_user
)
from datetime import datetime

import os
print("DB PATH:", os.path.abspath("service.db"))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"


class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default="NEW")
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --------------------
# Database Model
# --------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default="user")

# --------------------
# Login Manager
# --------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --------------------
# Routes
# --------------------

@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and user.password == request.form["password"]:
            login_user(user)
            return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/request/new", methods=["GET", "POST"])
@login_required
def new_request():
    if request.method == "POST":
        req = ServiceRequest(
            title=request.form["title"],
            description=request.form["description"],
            user_id=current_user.id
        )
        db.session.add(req)
        db.session.commit()
        return redirect(url_for("dashboard"))

    return render_template("new_request.html")


@app.route("/dashboard")
@login_required
def dashboard():
    requests = ServiceRequest.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", requests=requests)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

