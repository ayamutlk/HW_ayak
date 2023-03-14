from project3.BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest




@pytest.mark.usefixtures("setup")
@pytest.mark.security
class TestSecurity(BaseClass):

    def test_login_correct(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//img[@src='../static/log-in.png']").click()

        setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your username']").send_keys("aya")

        setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']").send_keys("345")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert setup.find_element(By.XPATH, "//p[@class='error']").text == "Invalid username or password"
        print("the test sucsses")
        log = self.getLogger()
        log.info("The password and the user nam is correct")




    def test_login_error(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//img[@src='../static/log-in.png']").click()

        setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your username']").send_keys("aya")

        setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']").send_keys("123")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert setup.current_url == "http://127.0.0.1:5000/home"
        log = self.getLogger()
        log.info("The password and user nam is error will gaven msg: 'that error'")




    def test_delete_review(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//img[@src='/display/braveheart_.jpg']").click()
        comment_before_delete = setup.find_elements(By.XPATH, "//li")
        setup.find_element(By.XPATH, "//body/ol[2]/form[1]/button[1]").click()
        comment_after_delete = setup.find_elements(By.XPATH, "//li")
        assert len(comment_after_delete) < len(comment_before_delete), "passed"
        log = self.getLogger()
        log.info("The movie will deleted from the homepage")


    def test_search_nothing_found(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//input[@id='search']").send_keys("hi")
        setup.find_element(By.CSS_SELECTOR, "#submit").click()
        assert setup.find_element(By.XPATH, "//h1[normalize-space()='Nothing found']").text == "Nothing found"
        log = self.getLogger()
        log.info("The page of 'info' is opened")
        log.debug("")


    def test_title_homePage(self, setup):
        setup.get("http://127.0.0.1:5000")
        title= setup.find_element(By.CSS_SELECTOR, "h1").text
        assert title == "TO-SHOW", "passed"
        log = self.getLogger()
        log.info("The title of the home page is 'TO-SHOW'")
        log.debug("")

    # print(x)


    # def test_image_notFind(self, setup):
    #     setup.get("http://127.0.0.1:5000")
    #     setup.find_element(By.XPATH, "//img[@src='../static/log-in.png']").click()
    #
    #     setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your username']").send_keys("aya")
    #
    #     setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']").send_keys("123")
    #
    #     setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    #     setup.find_element(By.CSS_SELECTOR, ".button").click()
    #     setup.find_element(By.XPATH, "//button[@class='button']").click()
    #     setup.find_element(By.NAME, 'filename').send_keys("C:/Users/Administrator/Desktop/a.webp")
    #     setup.find_element(By.NAME, 'movie_title').send_keys("aya")
    #     setup.find_element(By.NAME, 'movie_title').send_keys("aya")
    #     setup.find_element(By.NAME, 'description').send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    #     setup.find_element(By.NAME, 'director').send_keys("kaabyia")
    #     setup.find_element(By.NAME, 'actor').send_keys("aya, jood, ali")
    #     setup.find_element(By.NAME, 'release_year').send_keys(2022)
    #     iframe_html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/wPmTp9up26w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    #     setup.find_element(By.NAME, 'video').send_keys(iframe_html)
    #     # driver.execute_script("arguments[0].innerHTML = arguments[1];", element, iframe_html)
    #     setup.find_element(By.XPATH, "//button[normalize-space()='ADD']").click()
    #     assert setup.current_url != "http://127.0.0.1:5000/movie_info/1"
    #



    # def test_add_director_with_S(self, setup):
    #     setup.get("http://127.0.0.1:5000")
    #     setup.find_element(By.XPATH, "//img[@src='../static/log-in.png']").click()
    #
    #     setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your username']").send_keys("aya")
    #
    #     setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']").send_keys("123")
    #
    #     setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    #     before_add = setup.find_elements(By.XPATH, "//div/a")
    #     setup.find_element(By.CSS_SELECTOR, ".button").click()
    #     setup.find_element(By.NAME, 'filename').send_keys("C:/Users/Administrator/Desktop/godfa2.jpg")
    #     setup.find_element(By.NAME, 'movie_title').send_keys("The Godfather Part II")
    #     setup.find_element(By.NAME, 'description').send_keys(
    #         "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.")
    #     setup.find_element(By.NAME, 'director').send_keys("Joseph Kosinski,Joseph Kosinski,Joseph Kosinski,Joseph Kosinski,Joseph Kosinski,Joseph Kosinski,Joseph Kosinski")
    #     setup.find_element(By.NAME, 'actor').send_keys("Al Pacino, Robert De Niro, Robert Duvall")
    #     setup.find_element(By.NAME, 'release_year').send_keys(1974)
    #     # define the HTML code for the iframe
    #     # inject the HTML code for the iframe into the element
    #     iframe_html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/wPmTp9up26w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    #     setup.find_element(By.NAME, 'video').send_keys(iframe_html)
    #     # driver.execute_script("arguments[0].innerHTML = arguments[1];", element, iframe_html)
    #     setup.find_element(By.XPATH, "//button[normalize-space()='ADD']").click()
    #     after_add = setup.find_elements(By.XPATH, "//div/a")
    #     assert len(after_add) == len(before_add), "the movie not added"



# def test_crossBrowser(crossBrowser):
#     print(crossBrowser)