from behave import when, then, given
from selenium.webdriver.common.by import By
import logging
import time
log_file = 'behave.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)

@given('The site "{url}" is open')
def go_to_url(context, url):
    context.driver.get(url)


@when('The user clicks on the "{movie}" image')
def click_on_movie_img(context, movie):
    for row in context.rows:
        if row[1] == movie:
            context.driver.find_element(By.XPATH, row[3]).click()

@when('The user clicks on the "{logo_homepage}"')
def click_on_logo_img(context, logo_homepage):
    for row in context.rows:
        if row[1] == logo_homepage:
            context.driver.find_element(By.CSS_SELECTOR, row[3]).click()



@then("The user should be navigated to the home page")
def cheek_url_movie(context):
    current_url = context.driver.current_url
    assert current_url == "http://127.0.0.1:5000/", f"Expected URL: http://127.0.0.1:5000/ but got {current_url}"
    logging.info("passed successfully to about HOME page")


