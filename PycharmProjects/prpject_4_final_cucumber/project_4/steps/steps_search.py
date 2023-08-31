from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By



# Step 1: Given the user is on the home page
@given('The user is on the home page')
def go_to_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://127.0.0.1:5000")

# Step 2: When the user enters the search term and clicks the search button
@when('The user enters "{search_term}" in the search field')
def enterTitle_movie_onSearchBar(context, search_term):
    search_input = context.driver.find_element(By.XPATH, "//input[@id='search']")
    search_input.clear()
    search_input.send_keys(search_term)

@when('Clicks the search button')
def click_search_button(context):
    search_button = context.driver.find_element(By.CSS_SELECTOR, "#submit")
    search_button.click()

# Step 3: Then the search results page should be displayed
@then('The search results page should be displayed')
def check_the_result(context):
    try:
        assert context.driver.find_element(By.XPATH, "//h1[normalize-space()='Toy Story']").text == "Toy Story"
    except NoSuchElementException:
        assert context.driver.find_element(By.XPATH, "//h1[normalize-space()='Nothing found']").text == "Nothing found"
    finally:
        context.driver.quit()
