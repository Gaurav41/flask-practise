from flask import Flask, request,jsonify
from flask.views import MethodView

app = Flask(__name__)

Users = [{
        "name": "Gaurav"
        },
        {"name": "Akshay"},
        {"name": "Prajakta"},
        {"name": "Anant"}]

def get_user(name):
    return [u for u in Users if u["name"]==name][0]


class User(MethodView):

    def get(self,user_name):
        if user_name:
            return  jsonify({"user":get_user(user_name)})
        else:
            return jsonify({"users":Users})

    def post(self):
        new_user_name = request.json["name"]
        user = {"name":new_user_name}
        Users.apppend(user)
        return jsonify({'user' : get_user(new_user_name)}), 201
    
    def put(self,username):
        user = get_user(username)
        new_user_name = request.json['name']
        user['name'] = new_user_name
        return jsonify({'user' : get_user(new_user_name)})
        

    def delete(self,username):
        user = get_user(username)
        Users.remove(user)
        return '', 204
        
user_view = User.as_view('user_api')
app.add_url_rule('/user', methods=['POST'], view_func=user_view)
app.add_url_rule('/user', methods=['GET'], defaults={'user_name' : None}, view_func=user_view)
app.add_url_rule('/user/<user_name>', methods=['GET', 'PUT', 'DELETE'], view_func=user_view)

