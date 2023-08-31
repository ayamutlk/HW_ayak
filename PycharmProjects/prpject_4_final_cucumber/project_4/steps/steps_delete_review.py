from behave import when, then, given
from selenium.webdriver.common.by import By
import logging
log_file = 'behave.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)

@given('The website "{url}" is opened')
def go_to_url(context, url):
    context.driver.get(url)

@when('The user clicks on the "{movie}" that choose')
def go_to_movie_page(context, movie):
    for row in context.rows:
        if row[1] == movie:
            context.driver.find_element(By.XPATH, row[3]).click()




@when('The user click on "{delete_review}" button')
def button_delete_review(context, delete_review):
    comment_before_delete = context.driver.find_elements(By.XPATH, "//li")
    for row in context.rows:
        if row[1] == delete_review:
            context.driver.find_element(By.XPATH, row[3]).click()
    comment_after_delete = context.driver.find_elements(By.XPATH, "//li")
    context.comment_before_delete = comment_before_delete
    context.comment_after_delete = comment_after_delete

@then("The number of reviews should decrease by 1")
def delete_review(context):
    assert len(context.comment_after_delete) < len(context.comment_before_delete)
    context.driver.quit()
    logging.info("the comment deleted")
