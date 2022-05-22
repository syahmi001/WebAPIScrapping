import os

from utils import get_json, get_article
from flask import Flask, render_template, request

from dotenv import load_dotenv

# App configuration and the upload folder path
app = Flask(__name__)

# Load .env variables. Bad practise to hardcode the values here.
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
URL = 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=' + API_KEY


# Defining paths for Flask app
# Path to the root of the app, index.html
@app.route('/', methods=['GET'])
def index():
    data = get_json(URL)
    return render_template('index.html', datas=data)


# Path to the specific info for each article
# Looping through article id to get the matching id
@app.route('/api/<int:id>/', methods=['GET'])
def article_info(id):
    data = get_article(id, URL)
    articles = data['results']
    try:
        for i in range(len(articles)):
            if articles[i]['id'] == id:
                matched_article = articles[i]
                return render_template('article.html', article=matched_article)
            else:
                pass
    except:
        return 'There might be issue with API limit or ID not found. Please wait for a bit and try again!'


# Returning error 404 if the page does not exist
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
