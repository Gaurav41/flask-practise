
# ImportError: cannot import name 'FlaskSerialize' from 'flask_serialize'

from flask_serialize import FlaskSerialize
from flask import Flask,jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/sqlalchemy_demo'
db = SQLAlchemy(app)

fs_mixin = FlaskSerialize(db)

class Book(db.Model,fs_mixin):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text)
  author = db.Column(db.Text)

  def __init__(self, title, author):
    self.title = title
    self.author = author

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add",methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form["title"]
        author = request.form['author']
        book1 = Book(name,author)
        db.session.add(book1)
        db.session.commit()
        return jsonify([{'id':book.id, 'title':book.title,'author':book.author}for book in Book.query.all()])
    else:
        return render_template('index.html')

@app.route("/books")
def books():
    # return jsonify(Book.query.all())
    # TypeError: Object of type Book is not JSON serializable
    return jsonify([{'id':book.id, 'title':book.title,'author':book.author}for book in Book.query.all()])

@app.route('/book/<int:book_id>')
@app.route('/books')
def items(item_id=None):
    return Book.get_delete_put_post(item_id)

if __name__ == "main":
    app.run(debug=True)
