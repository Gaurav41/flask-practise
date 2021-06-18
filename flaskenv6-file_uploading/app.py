from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "F:/Cuelogic/Training/5 Flask/Environments/flaskenv6-file_uploading/uploaded_files"

@app.route("/")
def upload():
    return render_template('upload.html')

@app.route("/uploader",methods = ["GET","POST"])
def uploader():
    if request.method == "POST":
        f = request.files["file"]
        location = os.path.join(app.config['UPLOAD_FOLDER'])
        f.save(location, secure_filename(f.filename))
        return "File Uploaded Successfully"


if __name__ == "main":
    app.run(debug=True)

