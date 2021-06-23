from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/sqlalchemy_demo'
db = SQLAlchemy(app)


class Users(db.Model):
    """This class represent Table in 
        database"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80),unique=False,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"User('{self.name}', '{self.username}', '{self.password}', '{self.email}')"


@app.route("/")
def index():
    print(Users.query.all())
    print(Users.query.first())
    return render_template("index.html")

@app.route("/login",methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return "login fun yet to be define"
        
    else:
        return render_template("login.html")


@app.route("/signup",methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']

        #add data to data base 
        entry = Users(name=name, username=username, password=password, email=email)
        db.session.add(entry)
        db.session.commit()

        
        return "Signup Done<a href='http://127.0.0.1:5000/login'>Clicl here for login</a>"
    else:
        return render_template("signup.html")

if __name__=="main":
    app.run(debug=True)
    