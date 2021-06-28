
#####  Environment: production

from flask import Flask, app,request,abort,render_template
from logging import FileHandler,WARNING
import logging

logging.basicConfig(filename="error_logs.log",level=logging.DEBUG)
#logging.basicConfig(filename="formated_error_logs.log",level=logging.DEBUG,
# format='%(asctime)s:%(levelname)s:%(message)s ' )

app = Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    print("inside index")
    # logging.debug("inside index (debug)")
    # logging.info("inside index (info)")
    # logging.warning("inside index (warning)")
    # logging.error("inside index (error)")
    # logging.critical("inside index (critical)")

    # abort(404)
    # return 5/0  
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    password = request.form['password']
    if user == "admin" and password == "admin" :
        
        app.logger.info('%s logged in successfully', user)
        # logging.debug("logged in successfully", user)
        return "Loggend in"
    else:
        app.logger.error('%s failed to log in', user)
        # logging.error("failed to log in", user)
        abort(401)


if __name__ == "main":
    app.run(debug=False)