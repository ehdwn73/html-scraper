from flask import Flask, request
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import jsbeautifier

app = Flask(__name__)
CORS(app)

@app.route('/')
def intro():
    return 'https://github.com/Gtwo2/html-scraper/blob/main/README.md'

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
    
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string:
                beautified_js = jsbeautifier.beautify(script.string)
                script.string.replace_with(beautified_js)
    
        standardized_html = soup.prettify()
    
        return standardized_html
    except requests.exceptions.RequestException as e:
        return f"ERROR : {str(e)}", 500
if __name__ == 'main':
    app.run()
