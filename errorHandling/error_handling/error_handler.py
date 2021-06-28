from flask import render_template
from flask import Request
import werkzeug
def not_found(e):
    print(e)
    print("code 404 not found")
    return render_template("404.html")

def service_unavailable(e):
    # app.logger.error(f"service unavailable:{e}, route{Request.url}")
    print("code 503 service unavailable")
    return render_template("503.html")

# Non-standard HTTP codes cannot be registered by code because they are not known 
# by Werkzeug. Instead, define a subclass of HTTPException with the appropriate code 
# and register and raise that exception class.

class InsufficientStorage(werkzeug.exceptions.HTTPException):
    code = 507
    description = 'Not enough storage space.'

    def handle_507(e):
        return "Not enough storage space."


