from flask import Flask
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/sqlalchemy_demo'

ma = Marshmallow(app)

from models import db

if __name__ == "__main__":
    app.run(debug=True)
