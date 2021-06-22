from flask import Flask, Blueprint, render_template

user_bp = Blueprint("user_bp",__name__,template_folder='templates')

@user_bp.route("/list")
def list():
    return render_template("user/list.html")
    # return "user list"



