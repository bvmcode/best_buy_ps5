import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import yagmail

load_dotenv()
USERNAME = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PWD")
URL = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"


def email():
    yag = yagmail.SMTP(USERNAME, PASSWORD)
    yag.send(USERNAME, "PS5 Available - Best Buy", URL)


def get_status():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(executable_path='/home/bvmcode/best_buy_ps5/chromedriver', chrome_options=options)
    driver.get(URL)
    contents = driver.find_element_by_class_name("add-to-cart-button")
    if contents.text == "Add to Cart":
        email()

    driver.close()


if __name__ == "__main__":
    get_status()
