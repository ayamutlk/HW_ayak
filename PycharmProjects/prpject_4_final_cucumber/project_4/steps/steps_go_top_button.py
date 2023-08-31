from behave import when, then, given
from selenium.webdriver.common.by import By
import logging
log_file = 'behave.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)

@given('The website "{url}" is open')
def go_to_url(context, url):
    context.driver.get(url)


@when('I click on the "{movie}" from the homepage')
def click_on_theMovie(context, movie):
    for row in context.rows:
        if row[1] == movie:
            context.driver.find_element(By.XPATH, row[3]).click()



@when('I click on the "{top_button}" in info page')
def click_goTop_button(context, top_button):
    for row in context.rows:
        if row[1] == top_button:
            context.driver.find_element(By.CSS_SELECTOR, row[3]).click()

@then('I should be scrolled to the top of the page')
def cheek_upPage(context):
    context.driver.execute_script('window.scrollTo(0, 0);')
    scroll_position = context.driver.execute_script('return window.pageYOffset;')
    assert scroll_position == 0
    logging.info("passed successfully go to TOP the page")
