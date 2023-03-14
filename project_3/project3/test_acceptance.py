
from selenium.webdriver.common.by import By
import pytest
from BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Acceptance
class TestAcceptance(BaseClass):

        def test_add_movie(self, setup):
                setup.get("http://127.0.0.1:5000")
                setup.find_element(By.CSS_SELECTOR, "img[src='../static/log-in.png']").click()

                setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your username']").send_keys("aya")

                setup.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']").send_keys("123")

                setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                before_add = setup.find_elements(By.XPATH, "//div/a")
                setup.find_element(By.CSS_SELECTOR, ".button").click()
                setup.find_element(By.CSS_SELECTOR, "input[name='filename']").send_keys("C:/Users/Administrator/Desktop/godfa2.jpg")
                setup.find_element(By.CSS_SELECTOR, "input[name='movie_title'").send_keys("The Godfather Part II")
                setup.find_element(By.CSS_SELECTOR, "textarea[name='description']").send_keys(
                        "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.")
                setup.find_element(By.CSS_SELECTOR, "input[name='director']").send_keys("Francis Ford Coppola")
                setup.find_element(By.CSS_SELECTOR, "input[name='actor']").send_keys("Al Pacino, Robert De Niro, Robert Duvall")
                setup.find_element(By.CSS_SELECTOR, "input[name='release_year']").send_keys(1974)
                # define the HTML code for the iframe
                # inject the HTML code for the iframe into the element
                iframe_html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/wPmTp9up26w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
                setup.find_element(By.CSS_SELECTOR, "input[name='video']").send_keys(iframe_html)
                # driver.execute_script("arguments[0].innerHTML = arguments[1];", element, iframe_html)
                setup.find_element(By.XPATH, "//button[normalize-space()='ADD']").click()
                setup.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                setup.get_screenshot_as_file("add_movie.png")
                after_add = setup.find_elements(By.XPATH, "//div/a")
                assert len(after_add) > len(before_add), "the movie added"
                log = self.getLogger()
                log.info("The page of info_movie is opened")




        def test_search_capital_smoll(self, setup):
                setup.get("http://127.0.0.1:5000")

                setup.find_element(By.XPATH, "//input[@id='search']").send_keys("toy story")
                setup.get_screenshot_as_file("search.png")


                setup.find_element(By.CSS_SELECTOR, "#submit").click()
                setup.get_screenshot_as_file("searh1.png")

                setup.find_element(By.CSS_SELECTOR, "img[alt='logo']").click()

                setup.find_element(By.XPATH, "//input[@id='search']").send_keys("Toy story")
                setup.find_element(By.CSS_SELECTOR, "#submit").click()
                setup.get_screenshot_as_file("searh2.png")
                assert setup.find_element(By.XPATH, "//h1[normalize-space()='Toy Story']").text == "Toy Story"
                log = self.getLogger()
                log.info("The page of 'info' is opened")



        def test_delete_movie(self, setup):
                setup.get("http://127.0.0.1:5000")
                before_delete = setup.find_elements(By.XPATH, "//div/a")
                setup.find_element(By.XPATH, "(//img)[18]").click()
                # driver.get("http://127.0.0.1:5000/movie_info/11")
                setup.find_element(By.XPATH, "//a[normalize-space()='Delete']").click()
                after_delete = setup.find_elements(By.XPATH, "//div/a")
                setup.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                setup.get_screenshot_as_file("delete_movie.png")
                assert len(after_delete) < len(before_delete), "the movie is not delete"
                log = self.getLogger()
                log.info("The page of 'info' is opened")


        def test_update_title(self, setup):
                setup.get("http://127.0.0.1:5000")

                setup.find_element(By.XPATH, "(//img)[12]").click()
                setup.find_element(By.XPATH, "//a[normalize-space()='alter']").click()
                setup.find_element(By.XPATH, "//input[@name='movie_title']").send_keys("Top Gun: Maverick")
                setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                setup.get_screenshot_as_file("add_movie.png")
                assert setup.find_element(By.CSS_SELECTOR, "h1").text == "Top Gun: Maverick"
                log = self.getLogger()
                log.info("The page of 'info' is opened")


        def test_add_comment(self, setup):
                setup.get("http://127.0.0.1:5000")
                setup.find_element(By.XPATH, "(//img)[12]").click()
                before_new_comment = setup.find_elements(By.XPATH, "(//li[contains(text(),'Name:')])")
                setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Talia")
                setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("Awesome")
                setup.find_element(By.CSS_SELECTOR, "label[title='Awesome']").click()
                setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                setup.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                setup.get_screenshot_as_file("add_comment.png")
                after_new_comment = setup.find_elements(By.XPATH, "(//li[contains(text(),'Name:')])")
                assert len(after_new_comment) > len(before_new_comment), "the comment is not add"
                log = self.getLogger()
                log.info("The page of 'contact us' is opened")
                log = self.getLogger()
                log.info("The page of 'info' is opened")

# def test_crossBrowser(crossBrowser):
#         print(crossBrowser)