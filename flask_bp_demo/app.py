from flask import Flask, request,render_template
from flask_bp_demo.auth.auth import auth_bp
from flask_bp_demo.user.user import user_bp


app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp,url_prefix='/user')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "main":
    app.run()
