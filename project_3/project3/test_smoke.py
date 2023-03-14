from project3.BaseClass import BaseClass
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
@pytest.mark.smoke
class TestSmoke(BaseClass):

    def test_to_info_page(self, setup):

        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.CSS_SELECTOR, "img[src='/display/braveheart_.jpg']").click()
        assert setup.current_url == "http://127.0.0.1:5000/movie_info/1"
        log = self.getLogger()
        log.info("The page of 'info' is opened")
        # log.cretical("The page of 'info' is not opened")



    def test_logo_img(self,setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "(//img)[12]").click()
        setup.find_element(By.CSS_SELECTOR, "img[alt='logo']").click()
        assert setup.current_url == "http://127.0.0.1:5000/"
        log = self.getLogger()
        log.info("The page of 'info' is opened")
        # log.cretical("The page of 'info' is not opened")
        log.debug("")



    def test_go_about_page(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//img[@alt='logo']").click()
        assert setup.current_url == "http://127.0.0.1:5000/about_me"
        log = self.getLogger()
        log.info("The page of 'about' is opened")



    def test_go_login_page(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.CSS_SELECTOR, "img[src='../static/log-in.png']").click()
        assert setup.current_url == "http://127.0.0.1:5000/login"
        log = self.getLogger()
        log.info("The page of 'login' is opened")
        # log.cretical("The page of 'info' is not opened")
        log.debug("")



    def test_search_movie(self,setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "//input[@id='search']").send_keys("Toy story")
        setup.find_element(By.CSS_SELECTOR, "#submit").click()
        assert setup.find_element(By.XPATH, "//h1[normalize-space()='Toy Story']").text == "Toy Story"
        print("the search pass")
        log = self.getLogger()
        log.info("The search on title of movie will gaven the info page for this movie")
        log.debug("")





# def test_crossBrowser(crossBrowser):
#     print(crossBrowser)
