from flask import Flask, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def intro():
    return '/scrape?url=target url'

@app.route('/scrape')
def scrape():
    target_url = request.args.get('url')
    if not target_url:
        return "ERROR : URL not specified", 400

    try:
        response = requests.get(target_url)
        response.raise_for_status()
        html = response.text
        return html
    except requests.exceptions.RequestException as e:
        return f"ERROR : {str(e)}", 500

if __name__ == '__main__':
    app.run()

