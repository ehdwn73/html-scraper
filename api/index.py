from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
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
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get(target_url)
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        html = driver.page_source

        driver.quit()

        soup = BeautifulSoup(html, 'html.parser')

        scripts = soup.find_all('script')
        for script in scripts:
            if script.string:
                beautified_js = jsbeautifier.beautify(script.string)
                script.string.replace_with(beautified_js)

        standardized_html = soup.prettify()

        return standardized_html
    except Exception as e:
        return f"ERROR : {str(e)}", 500

if __name__ == '__main__':
    app.run()
