from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/sqlalchemy_demo'


db = SQLAlchemy(app)
ma = Marshmallow(app)

class User1(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120),nullable=False)

    # def __repr__(self):
    #     return f"id:{self.id}, name:{self.name}"

class Reward(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    reward_name = db.Column(db.String(50))
    user_id = db.Column(db.Integer,db.ForeignKey('user1.id'))
    user = db.relationship('User1',backref="rewards")


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        #model = User1

class RewardSchema(ma.Schema):
    class Meta:
        model = Reward

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/")
def index():
    return "wlc to API"

@app.route("/api/users")
def all_users_data():

    #Single user data

    # user_one = User1.query.first()
    # output = user_schema.dump(user_one)
    # print("output:", output)
    # return jsonify({"First Users": output})
    # {"First Users": {"id": 1, "name": "user one"}}

    #All users data

    all_users = User1.query.all()
    output = users_schema.dump(all_users)
    print("output:", output)
    return jsonify({"All Users":output})
    #{"All Users":[{"id":1,"name":"user one"},{"id":2,"name":"user two"},
    # {"id":3,"name":"Gaurav"},{"id":4,"name":"Akshay"}]}

@app.route("/api/users/<id>")
def user_detail(id):
    user = User1.query.get(id)
    return user_schema.dump(user)


if __name__ == "__main__":
    app.run(debug=True)


# >>> db.create_all()
# >>> from app import db,User1,Reward
# >>> one = User1(name="Gaurav")
# >>> two = User1(name="Akshay")
# >>> db.session.add_all([one,two])
# >>> db.session.commit()

# >>> first = Reward(reward_name="R1",user=one)
# >>> second = Reward(reward_name="R2",user=one)
# >>> third = Reward(reward_name="R3",user=two)

