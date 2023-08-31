# # from behave import when, then, given
# # from selenium.webdriver.common.by import By
# # import logging
# # log_file = 'behave.log'
# # file_handler = logging.FileHandler(log_file)
# # file_handler.setLevel(logging.INFO)
# # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # file_handler.setFormatter(formatter)
# # logging.getLogger('').addHandler(file_handler)
# #
# # @given('The user is on the page url "{url}"')
# # def go_to_url(context, url):
# #     context.driver.get(url)
# #
# # @then('Click on "{login}"')
# # def click_logo_login(context, login):
# #     for row in context.rows:
# #         if row[1] == login:
# #             if row[4] == "XPATH":
# #                 context.driver.find_element(By.XPATH, row[3]).click()
# #             elif row[4] == "CSS_SELECTOR":
# #                 context.driver.find_element(By.CSS_SELECTOR, row[3]).click()
# #     # context.driver.find_element(By.XPATH, "//img[@src='../static/log-in.png']").click()
# #
# #
# #
# # @when('The user enter the data')
# # def enter_credentials(context):
# #     for row in context.rows:
# #         if row[1] == "username":
# #             context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(row[2])
# #         elif row[1] == "password":
# #             context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(row[2])
# #         elif row[1] == "password-inco":
# #             context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(row[2])
# #
# #
# #
# #     for row in context.rows:
# #         if row[1] == "username":
# #             if row[4] == "CSS_SELECTOR":
# #                 context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(username)
# #         elif row[1] == "password":
# #             if row[4] == "CSS_SELECTOR":
# #                 context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(password)
# #
# #     #
# #     # for row in context.rows:
# #     #     if row[1] == "username":
# #     #         if row[4] == "CSS_SELECTOR":
# #     #             context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(username)
# #     #     elif row[1] == "password":
# #     #         if row[4] == "CSS_SELECTOR":
# #     #             context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(password)
# #
# #     # username_input = context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your username']")
# #     # username_input.send_keys(username)
# #     # password_input = context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']")
# #     # password_input.send_keys(password)
# #
# # @when('Clicks the "{login_button}"')
# # def click_login_button(context, login_button):
# #     for row in context.rows:
# #         if row[1] == login_button:
# #             if row[4] == "XPATH":
# #                 context.driver.find_element(By.XPATH, row[3]).click()
# #             elif row[4] == "CSS_SELECTOR":
# #                 context.driver.find_element(By.CSS_SELECTOR, row[3]).click()
# #     # login_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
# #     # login_button.click()
# #
# #
# # # @then('The user should see indicating login {status}')
# # # def check_login_status(context, status):
# # #     if status == "incorrect":
# # #         error_message = context.driver.find_element(By.XPATH, "//p[@class='error']")
# # #         assert error_message.text == "Invalid username or password"
# # #     elif status == "correct":
# # #         assert context.driver.current_url == "http://127.0.0.1:5000/home"
# # @then('The user should see indicating login {status}')
# # def check_login_status(context, status):
# #     if status == "incorrect":
# #         error_message = context.driver.find_element(By.XPATH, "//p[@class='error']")
# #         assert error_message.text == "Invalid username or password"
# #     elif status == "correct":
# #         assert context.driver.current_url == "http://127.0.0.1:5000/home"
# #
# #
# #
# #
# #
# #
# #     # if status == "incorrect":
# #     #     context.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
# #     # elif status == "correct":
# #     #     context.driver.quit()
# from behave import when, then, given
# from selenium.webdriver.common.by import By
# import logging
#
# # log_file = 'behave.log'
# # file_handler = logging.FileHandler(log_file)
# # file_handler.setLevel(logging.INFO)
# # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # file_handler.setFormatter(formatter)
# # logging.getLogger('').addHandler(file_handler)
# #
# # @given('The user is on the page url "{url}"')
# # def go_to_url(context, url):
# #     context.driver.get(url)
# #
# # @then('Click on "{login}"')
# # def click_logo_login(context, login):
# #     for row in context.rows:
# #         if row[1] == login:
# #             if row[4] == "XPATH":
# #                 context.driver.find_element(By.XPATH, row[3]).click()
# #             elif row[4] == "CSS_SELECTOR":
# #                 context.driver.find_element(By.CSS_SELECTOR, row[3]).click()
# #
# # @when('The user enter the data <username>')
# # def enter_credentials(context, username):
# #     for row in context.rows:
# #         if row[1] == "username":
# #             if row[4] == "CSS_SELECTOR":
# #                 context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(username)
# #         elif row[1] == "password":
# #             if row[4] == "CSS_SELECTOR":
# #                 context.driver.find_element(By.CSS_SELECTOR, row[3]).send_keys(password)
# #
# # @when('Clicks the "{login_button}"')
# # def click_login_button(context, login_button):
# #     for row in context.rows:
# #         if row[1] == login_button:
# #             if row[4] == "XPATH":
# #                 context.driver.find_element(By.XPATH, row[3]).click()
# #             elif row[4] == "CSS_SELECTOR":
# #                 context.driver.find_element(By.CSS_SELECTOR, row[3]).click()
# #
# # @then('The user should see indicating login {status}')
# # def check_login_status(context, status):
# #     if status == "incorrect":
# #         error_message = context.driver.find_element(By.XPATH, "//p[@class='error']")
# #         assert error_message.text == "Invalid username or password"
# #     elif status == "correct":
# #         assert context.driver.current_url == "http://127.0.0.1:5000/home"
# #
#
#
# from behave import when, then, given
# from selenium.webdriver.common.by import By
# import logging
#
# log_file = 'behave.log'
# file_handler = logging.FileHandler(log_file)
# file_handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logging.getLogger('').addHandler(file_handler)
#
#
# @given('The user is on the page url "{url}"')
# def go_to_url(context, url):
#     context.driver.get(url)
#
#
# @then('Click on "{login}"')
# def click_logo_login(context, login):
#     for row in context.table:
#         if row['header'] == login:
#             if row['selector_type'] == "XPATH":
#                 context.driver.find_element(By.XPATH, row['selector']).click()
#             elif row['selector_type'] == "CSS_SELECTOR":
#                 context.driver.find_element(By.CSS_SELECTOR, row['selector']).click()
#
#
# @when('The user enter the data')
# def enter_credentials(context):
#     for row in context.table:
#         if row['header'] == "username":
#             context.driver.find_element(By.CSS_SELECTOR, row['selector']).send_keys(row['value'])
#         elif row['header'] == "password":
#             context.driver.find_element(By.CSS_SELECTOR, row['selector']).send_keys(row['value'])
#         elif row['header'] == "password-inco":
#             context.driver.find_element(By.CSS_SELECTOR, row['selector']).send_keys(row['value'])
#
#
# @when('Clicks the "{login_button}"')
# def click_login_button(context, login_button):
#     for row in context.table:
#         if row['header'] == login_button:
#             if row['selector_type'] == "XPATH":
#                 context.driver.find_element(By.XPATH, row['selector']).click()
#             elif row['selector_type'] == "CSS_SELECTOR":
#                 context.driver.find_element(By.CSS_SELECTOR, row['selector']).click()
#
#
# @then('The user should see indicating login {status}')
# def check_login_status(context, status):
#     if status == "incorrect":
#         error_message = context.driver.find_element(By.XPATH, "//p[@class='error']")
#         assert error_message.text == "Invalid username or password"
#     elif status == "correct":
#         assert context.driver.current_url == "http://127.0.0.1:5000/home"


from behave import when, then, given
from selenium.webdriver.common.by import By
import logging

log_file = 'behave.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)


@given('The user is on the page url "{url}"')
def go_to_url(context, url):
    context.driver.get(url)

@then('Click on "login"')
def click_login(context):

    context.driver.find_element(By.XPATH, "//img[@src='../static/log-in.png']").click()

@when('The user enters {username} and {password}')
def enter_credentials(context, username, password):
    username_input = context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your username']")
    username_input.send_keys(username)
    password_input = context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']")
    password_input.send_keys(password)

@when('The user clicks the "login button"')
def click_login_button(context):
    context.driver.find_element(By.XPATH, "(//button[normalize-space()='Sign in'])[1]").click()

@then('The user should see an indication of login {status}')
def check_login_status(context, status):
    if status == "correct":
        assert context.driver.current_url == "http://127.0.0.1:5000/home"
    elif status == "correct":
        error_message = context.driver.find_element(By.XPATH, "//p[@class='error']")
        assert error_message.text == "Invalid username or password"
