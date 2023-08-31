from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3
def before_all(context):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(3)
    context.driver = driver
    con = sqlite3.connect("movies_site.db")
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM data_indicators")
    rows = cursorObj.fetchall()
    context.rows = rows
    # cursorObj.execute("SELECT * FROM btn_indicators")
    # rows_btn = cursorObj.fetchall()
    # context.rows = rows_btn

    # cursorObj.execute("SELECT * FROM login_indicators")
    # rows_login = cursorObj.fetchall()
    # context.rows = rows_login