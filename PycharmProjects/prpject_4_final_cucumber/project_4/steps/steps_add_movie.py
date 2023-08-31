
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from behave import when, given, then
from webdriver_manager.chrome import ChromeDriverManager
#
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# service_obj = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#
# @given('the site "{url}" is opened')
# def go_to_url(context, url):
#     driver.get(url)
#     context.driver = driver
#
# @then("click on log in logo")
# def go_to_login_page(context):
#     context.driver.find_element(By.XPATH, "(//img[@alt='logo'])[2]").click()
#
# @then("put the username and put the password")
# def put_the_password(context):
#     context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your username']").send_keys("aya")
#     context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']").send_keys("123")
#     context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#
#
#
# @then("click on the add movie button")
# def click_in_add_button(context):
#     context.driver.find_element(By.CSS_SELECTOR, ".button").click()
#


from behave import when, then, given
from selenium.webdriver.common.by import By
import logging
log_file = 'behave.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)
@given("Open web application")
def open_web(context):
    context.driver.get("http://127.0.0.1:5000")

@then("click on log in logo")
def go_to_login_page(context):
    context.driver.find_element(By.XPATH, "(//img[@alt='logo'])[2]").click()

@then("put the username and put the password")
def put_the_password(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your username']").send_keys("aya")
    context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']").send_keys("123")
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

@when("Navigate to add movie button")
def navigate_to_add_data(context):
    context.driver.find_element(By.CSS_SELECTOR, ".button").click()



@when("Click on ADD button")
def click_add(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='ADD']").click()

@then("Validate end is bigger than beginning")
def final_validation(context):
    assert context.begin_images < context.end_images, "The movie is not added"
    logging.info("passed successfully")

#################################################
@when('Add data to "{data_type}"')
def add_data(context, data_type):
    for row in context.rows:
        if row[1] == data_type:
            context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(row[2])
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.get_screenshot_as_file("add_movie.png")

###################################
@then('Count "{elem}" in the "{status}"')
def count_img_begin(context, elem, status):
    if status == "beginning":
        context.begin_images = len(context.driver.find_elements(By.TAG_NAME, elem))
    elif status == "end":
        context.end_images = len(context.driver.find_elements(By.TAG_NAME, elem))
