from flask import Flask,Request,Response
from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/sqlalchemy_demo'

db = SQLAlchemy(app)

#create a model class
# This mixin adds .to_dict() method to model instances. 

class Employee(db.Model,SerializerMixin):
    non_sql_field = 5
    def just_demo(self):
        return 'hi'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(45),unique=False,nullable=True)
    email = db.Column(db.String(45),unique=True,nullable=True)

    # serialize_only = ('id',)
    # {"id":1}
    #serialize_rules = ('just_demo',)
    #{"email":"gp@gmail.com","id":1,"just_demo":"hi","name":"Gaurav"}
    # same as 
    # item.to_dict(only=('non_sql_field', 'method', 'somefield'))
    def __repr__(self) -> str:
        return f"Employess id: {self.id} Name: {self.name} email:{self.email} "

@app.route("/")
def index():
    try:
        emp=Employee(name="Ak5",email="ak5@gmail.com")
        db.session.add(emp)
        db.session.commit()
        result = "Success"
    except:
        print('error')
        result = "failed"
    return "hi"

@app.route("/do",methods = ["GET","POST"])
def operations():
    # Employess id: 1 Name: Gaurav email:gp@gmail.com 
    result = Employee.query.filter(Employee.name=="Gaurav").one()
    #{'id': 1, 'email': 'gp@gmail.com', 'name': 'Gaurav'}
    result = result.to_dict()
    # result = result.to_dict(rules=('non_sql_field','just_demo',))
    # {"email":"gp@gmail.com","id":1,"just_demo":"hi","name":"Gaurav","non_sql_field":5}
    # result = result.to_dict(only=('non_sql_field','just_demo',))
    # {"just_demo":"hi","non_sql_field":5}
    # result = result.to_dict(only=('non_sql_field','just_demo',))
    # {"just_demo":"hi","non_sql_field":5}


    print(result)
    return result


if __name__ == 'main':
    app.run(debug=True)
