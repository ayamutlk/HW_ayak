from behave import when, then, given
from selenium.webdriver.common.by import By
import logging
log_file = 'behave.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)

@given('Open the site "{url}"')
def go_to_url(context, url):
    context.driver.get(url)

@when('I click on the logo "{about}" from homepage up the page')
def click_on_logo(context, about):
    for row in context.rows:
        if row[1] == about:
            context.driver.find_element(By.XPATH, row[3]).click()


@then('I am taken to the About Me page')
def cheek_about_page(context):
    assert context.driver.current_url == "http://127.0.0.1:5000/about_me"
    logging.info("passed successfully to about me page")



