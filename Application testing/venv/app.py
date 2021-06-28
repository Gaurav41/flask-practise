from flask import Flask,request,Response,render_template,jsonify
from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/sqlalchemy_demo'

db = SQLAlchemy(app)

#create a model class
# This mixin adds .to_dict() method to model instances. 

class Tester(db.Model,SerializerMixin):

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(45),unique=False,nullable=True)
    email = db.Column(db.String(45),unique=True,nullable=True)
    password = db.Column(db.String(45))


    # def __repr__(self) -> str:
    #     return f"Employess id: {self.id} Name: {self.username} email:{self.email} "


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup",methods = ["GET","POST"])
def signup():
    if request.method == "POST":
        try:
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            print(username,email,password)
            emp=Tester(username=username,email=email,password=password)
            db.session.add(emp)
            db.session.commit()
            # result = "Success"
            result = render_template("login.html")

        except Exception as e:
            print('error')
            print(e)
            # result = "Signup failed"
            msg = "Signup failed"
            result = render_template("signup.html",msg=msg)
        return result
    else:
        return render_template("signup.html")


@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        
        try:
            username = request.form["username"]
            password = request.form["password"]
            result = Tester.query.filter(and_(Tester.username==username,Tester.password==password))
            return result.one().to_dict()

        except NoResultFound as e:
            print(e)
            return render_template("login.html")

        except Exception as e:
            print('error')
            print(e)
            # result = "Signup failed"
            msg = "login failed"
            return render_template("login.html",msg=msg)
             
    else:
        return render_template("login.html")


@app.route("/get_all",methods = ["GET"])
def operations():
    result = Tester.query.all()

    for t in result:
        print(result)
    return json.dumps(result)


if __name__ == 'main':
    app.run(debug=True)
