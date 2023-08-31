from behave import when, then, given
from selenium.webdriver.common.by import By
import logging
from selenium.common import NoSuchElementException

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

###############################################################################################

@then("click on login logo on homepage")
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

##########################################################################################################3
#alter

@when('Click on the "{detals}')
def step_1_click_alter(context, detals):
    for row in context.rows:
        if row[1] == detals:
            if row[4] == "XPATH":
                context.driver.find_element(By.XPATH, row[3]).click()
            elif row[4] == "CSS_SELECTOR":
                context.driver.find_element(By.CSS_SELECTOR, row[3]).click()


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

####################################################################################################
#delete review



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
####################################################################################################
#about


@when('I click on the logo "{about}"')
def click_on_logo(context, about):
    for row in context.rows:
        if row[1] == about:
            context.driver.find_element(By.XPATH, row[3]).click()


@then('I am taken to the About Me page')
def cheek_about_page(context):
    assert context.driver.current_url == "http://127.0.0.1:5000/about_me"
    logging.info("passed successfully to about me page")

########################################################################33
#top button


@when('I click on the "{movie}" from the homepage')
def click_on_theMovie(context, movie):
    for row in context.rows:
        if row[1] == movie:
            context.driver.find_element(By.XPATH, row[3]).click()



@when('I click the "{top_button}"')
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

#######################################################################################################3
#logo home page


@when('The user clicks on the "{movie}" image')
def click_on_movie_img(context, movie):
    for row in context.rows:
        if row[1] == movie:
            if row[4] == "XPATH":
                context.driver.find_element(By.XPATH, row[3]).click()
            elif row[4] == "CSS_SELECTOR":
                context.driver.find_element(By.CSS_SELECTOR, row[3]).click()

@when('The user clicks on the "{logo_homepage}"')
def click_on_logo_img(context, logo_homepage):
    for row in context.rows:
        if row[1] == logo_homepage:
            context.driver.find_element(By.XPATH, row[3]).click()


@then("The user should be navigated to the home page")
def cheek_url_movie(context):
    current_url = context.driver.current_url
    assert current_url == "http://127.0.0.1:5000/", f"Expected URL: http://127.0.0.1:5000/ but got {current_url}"
    logging.info("passed successfully to about HOME page")

#######################################################################################################
#search


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