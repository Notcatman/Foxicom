from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from email_validator import validate_email, EmailNotValidError
from flask import url_for, redirect, render_template, flash, request, Blueprint, session
from models import db, User


#es aris bluprinti da nebismieri saxelis darkmeva segvizlia, me davarkvi 'log'
#es aris anu naxet roca saitze sedixart da magalitad weria: RameSaiti/users/990912/settings
#anu blueprints gadaecema 'users' da kovel jerze ar gviwevs wera 'app.route('/users) radgan blueprinti koveltvis dauwers magas win
log = Blueprint('log', __name__)


#aq ukve iwereba im blueprintis saxeli da ara 'app'...
@log.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        #es mere davamate, es amowmebs emails, radgan userma ucnauri da ara emailis msgavsi ram ar chaweros
        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError as n:
            flash(str(n))
            return render_template("register.html")


        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("This username is taken. Please choose another")
            return redirect(url_for("log.register"))
        
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash("This email is taken. Please enter another")
            return render_template("register.html")
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successfull. Please log in")
        return redirect(url_for("log.login"))

    return render_template("register.html")

@log.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            flash("Logged in successfully")
            session['cart'] = []
            login_user(user)
            return redirect(url_for("routes.home"))
        else:
            flash("Username or password is incorrect!")

    return render_template("login.html")

@log.route("/logout")
@login_required
def logout():
    logout_user()
    session['cart'] = []
    flash("Logged out successfully")
    return redirect(url_for("routes.home"))

