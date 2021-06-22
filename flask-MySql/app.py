from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
# import pyyaml

app = Flask(__name__)
app.config['DEBUG']=True

#config db
# db = pyyaml.load(open("db.yaml"))
# app.config['MYSQL_HOST']= db['mysql_host']
# app.config['MYSQL_PASSWORD']=db['mysql_password']
# app.config['MYSQL_USER']= db['mysql_user']
# app.config['MYSQL_DB']=db['mysql_db']
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_PASSWORD']="root"
app.config['MYSQL_USER']="root"
app.config['MYSQL_DB']="flaskapp"
mysql = MySQL(app)

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        # return "<h1>hi"+name+"<h1>"
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name,email) VALUES(%s,%s)",(name,email))
        mysql.connection.commit()
        return redirect("/users")
    else:
        return render_template("index.html")

@app.route("/users",methods=["POST","GET"])
def users():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM users")
    if result > 0:
        users_details = cur.fetchall()
        
    return render_template("users.html", users_details = users_details)

if __name__ == 'main':
    app.run(debug=True)
