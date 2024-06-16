from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def intro():
    return '/scrape?url=target_url'

@app.route('/scrape')
def scrape():
    target_url = request.args.get('url')
    if not target_url:
        return "ERROR : URL not specified", 400

    try:
        response = requests.get(target_url)
        response.raise_for_status()
        html = response.text

        soup = BeautifulSoup(html, 'html5lib')
        standardized_html = soup.prettify()

        return standardized_html
    except requests.exceptions.RequestException as e:
        return f"ERROR : {str(e)}", 500

if __name__ == '__main__':
    app.run()
