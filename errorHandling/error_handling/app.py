from flask import Flask, app,request,abort,render_template
import error_handler
app = Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    # abort(503)
    # raise error_handler.InsufficientStorage()

    return render_template("index.html")

# @app.errorhandler(404)
# def not_found(e):
#     print(e)
#     return render_template("404.html")

# @app.errorhandler(503)
# def service_unavailable(e):
#     app.logger.error(f"service unavailable:{e}, route{request.url}")
#     return render_template("503.html")

# registering error handlers.
app.register_error_handler(404,error_handler.not_found)
app.register_error_handler(503,error_handler.service_unavailable)

# raise error_handler.InsufficientStorage()
app.register_error_handler(error_handler.InsufficientStorage,error_handler.InsufficientStorage.handle_507)

if __name__ == "main":
    app.run(debug=False)
