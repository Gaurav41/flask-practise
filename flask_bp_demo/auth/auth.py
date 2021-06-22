from flask import Flask,Blueprint,render_template

auth_bp = Blueprint('auth_bp', __name__,template_folder='templates')

@auth_bp.route('/login')
def login():
    # return "Login"
    return render_template("auth/login.html")

@auth_bp.route('/signup')
def signup():
    # return "signup"
    return render_template("auth/signup.html")