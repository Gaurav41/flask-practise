from flask import Flask, render_template,request,make_response

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html") 

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
        result = request.form
        abcd = 100
        resp = make_response(render_template("result.html",result = result))
        return resp

if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)