from behave import when, then, given
from selenium.webdriver.common.by import By
import logging
log_file = 'behave.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)

@given('The movie site "{url}" is opened')
def go_to_url(context, url):
    context.driver.get(url)

@when('I click on the "{movie}" in the website')
def go_to_movie_page(context, movie):
    for row in context.rows:
        if row[1] == movie:
            if row[4] == "XPATH":
                context.driver.find_element(By.XPATH, row[3]).click()
            elif row[4] == "CSS_SELECTOR":
                context.driver.find_element(By.CSS_SELECTOR, row[3]).click()


@when('I click on the "{alter_button}"')
def step_1_click_alter(context, alter_button):
    for row in context.rows:
        if row[1] == alter_button:
            if row[4] == "XPATH":
                context.driver.find_element(By.XPATH, row[3]).click()
            elif row[4] == "CSS_SELECTOR":
                context.driver.find_element(By.CSS_SELECTOR, row[3]).click()
#
# @when('Click on the "{detals}')
# def step_1_click_alter(context, detals):
#     for row in context.rows:
#         if row[1] == detals:
#             if row[4] == "XPATH":
#                 context.driver.find_element(By.XPATH, row[3]).click()
#             elif row[4] == "CSS_SELECTOR":
#                 context.driver.find_element(By.CSS_SELECTOR, row[3]).click()
# #
# @when('I enter "{text}" as the box bar {field_name}')
# def step_2(context, text, field_name):
#     if field_name == "director":
#         input_element = context.driver.find_element(By.XPATH, "//input[@name='director']")
#     elif field_name == "main actors":
#         input_element = context.driver.find_element(By.XPATH, "//input[@name='actor']")
#     elif field_name == "release year":
#         input_element = context.driver.find_element(By.XPATH, "//input[@name='release_year']")
#     input_element.clear()
#     input_element.send_keys(text)

@when('I enter "{text}" as the box bar {field_name}')
def step_2(context, field_name, text):
    for row in context.rows:
        if row[1] == field_name:
            context.driver.find_element(By.XPATH, row[3]).send_keys(text)


@then('I should see the new {field_name} on the page info movie')
def step_4(context, field_name):
    for row in context.rows:
        if row[1] == "director-alt":
            expected_text = row[2]
            actual_text = context.driver.find_element(By.CSS_SELECTOR, "body ol center h3:nth-child(2)").text
            assert actual_text == expected_text
        elif row[1] == "main actors-alt":
            expected_text = row[2]
            actual_text = context.driver.find_element(By.CSS_SELECTOR, "body ol center h3:nth-child(5)").text
            assert actual_text == expected_text
        elif row[1] == "release year-alt":
            expected_text = row[2]
            actual_text = context.driver.find_element(By.CSS_SELECTOR, "center h3:nth-child(8)").text
            assert actual_text == expected_text


