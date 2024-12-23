import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time

def scrapingWebsite(website):
    print("Launching chrome browser...")

    chromeDriverPath = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chromeDriverPath), options=options)

    try:
        driver.get(website)
        print("Page loaded :)")
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()

def extractBody(html):
    print("Extracting data...")
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body
    if body:
        return body.text
    return None


