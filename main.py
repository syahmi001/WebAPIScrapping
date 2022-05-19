import os
from utils.utils import get_json
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from dotenv import load_dotenv

# App configuration and the upload folder path
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


# Load .env variables
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
URL = 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=' + API_KEY


# Defining paths for Flask app
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/get-json/', methods=['GET'])
def hello_world():
    json_object = get_json(URL)
    return json_object


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
