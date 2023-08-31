from behave import when, then, given
from selenium.webdriver.common.by import By
import logging
log_file = 'behave.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)

@given('The site "{url}" is opened')
def go_to_url(context, url):
    context.driver.get(url)

@then('Click on the "{movie}"')
def go_to_movie_page(context, movie):
    for row in context.rows:
        if row[1] == movie:
            context.driver.find_element(By.XPATH, row[3]).click()



@when('The user adds a "{comment}" with name')
def add_new_name(context, comment):
    context.before_new_comment = context.driver.find_elements(By.XPATH, "(//li[contains(text(),'Name:')])")
    for row in context.rows:
        if row[1] == comment:
            if row[4] == "CSS_SELECTOR":
                context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(row[2])
            elif row[4] == "XPATH":
                context.driver.find_element(By.XPATH, row[3]).send_keys(row[2])


@when('New "{review_text}"')
def add_new_comment(context, review_text):
    for row in context.rows:
        if row[1] == review_text:
            context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(row[2])



@when('New "{rating}" stars')
def add_new_rating(context, rating):
    for row in context.rows:
        if row[1] == rating:
            context.driver.find_element(By.CSS_SELECTOR, row[3]).click()

@when('Click on the "{rating_button}"')
def click_on_add_comment_button(context, rating_button):
    for row in context.rows:
        if row[1] == rating_button:
            context.driver.find_element(By.CSS_SELECTOR, row[3]).click()
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.get_screenshot_as_file("add_comment.png")
    context.after_new_comment = context.driver.find_elements(By.XPATH, "(//li[contains(text(),'Name:')])")




@then("The comment is added successfully")
def check_comment_added(context):
    assert len(context.after_new_comment) > len(context.before_new_comment), "the comment was not added"
    logging.info("passed successfully")
