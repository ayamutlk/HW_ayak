from project3 import BaseClass
from selenium.webdriver.common.by import By
import pytest




@pytest.mark.usefixtures("setup")
@pytest.mark.functional
class TestFunctional(BaseClass):


    def test_top_button(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "(//img)[12]").click()
        setup.find_element(By.CSS_SELECTOR, "div[class='button']").click()
        # scroll to the top of the page using JavaScript
        setup.execute_script("window.scrollTo(0, 0);")
        # verify that the page has scrolled to the top by checking the scroll position
        scroll_position = setup.execute_script("return window.pageYOffset;")
        assert scroll_position == 0
        print("go to the top page")
        log = self.getLogger()
        log.info("The page will go to the top")




    def test_update_description(self, setup):
        setup.get("http://127.0.0.1:5000")

        setup.find_element(By.XPATH, "(//img)[12]").click()

        setup.find_element(By.XPATH, "//a[normalize-space()='alter']").click()
        setup.find_element(By.XPATH, "//textarea[@name='description']").send_keys("After thirty years, Maverick is still pushing the envelope as a top naval aviator, but must confront ghosts of his past when he leads TOP GUN's elite graduates on a mission that demands the ultimate sacrifice from those chosen to fly it.")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        assert setup.find_element(By.CSS_SELECTOR, ":nth-child(4) > h2:nth-child(4)").text == "After thirty years, Maverick is still pushing the envelope as a top naval aviator, but must confront ghosts of his past when he leads TOP GUN's elite graduates on a mission that demands the ultimate sacrifice from those chosen to fly it."
        log = self.getLogger()
        log.info("The update description will appear")



    def test_update_director(self, setup):
        setup.get("http://127.0.0.1:5000")


        setup.find_element(By.XPATH, "(//img)[12]").click()

        setup.find_element(By.XPATH, "//a[normalize-space()='alter']").click()
        setup.find_element(By.XPATH, "//input[@name='director']").send_keys("Joseph Kosinski")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert setup.find_element(By.CSS_SELECTOR, "body ol center h3:nth-child(2)").text == "Joseph Kosinski"
        print("the director update")
        log = self.getLogger()
        log.info("The update director will appear")



    def test_update_main_actors(self, setup):
        setup.get("http://127.0.0.1:5000")

        setup.find_element(By.XPATH, "(//img)[12]").click()

        setup.find_element(By.XPATH, "//a[normalize-space()='alter']").click()
        setup.find_element(By.XPATH, "//input[@name='actor']").send_keys("Cruise, Jennifer Connelly, Miles Teller")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert setup.find_element(By.CSS_SELECTOR, "body ol center h3:nth-child(5)").text == "Cruise, Jennifer Connelly, Miles Teller"
        log = self.getLogger()
        log.info("The update main actor will appear")


    def test_update_reales_year(self, setup):
        setup.get("http://127.0.0.1:5000")

        setup.find_element(By.XPATH, "(//img)[12]").click()

        setup.find_element(By.XPATH, "//a[normalize-space()='alter']").click()
        setup.find_element(By.XPATH, "//input[@name='release_year']").send_keys("2022")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert setup.find_element(By.CSS_SELECTOR, "center h3:nth-child(8)").text == "2022"
        print("the release year update")
        log = self.getLogger()
        log.info("The update title will appear")



    def test_reating_tow(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "(//img)[12]").click()
        setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ali")
        setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("good movie")
        setup.find_element(By.CSS_SELECTOR, "label[title='Good']").click()
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert setup.find_element(By.XPATH, "//body/ol[2]/h2[13]").text == "2"
        log = self.getLogger()
        log.info("The rating will appear two")



    def test_reating_three(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "(//img)[12]").click()
        setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("jood")
        setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("Very good movie")
        setup.find_element(By.CSS_SELECTOR, "label[title='Very good']").click()
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert setup.find_element(By.XPATH, "//body/ol[2]/h2[14]").text == "3"
        log = self.getLogger()
        log.info("The rating will appear three")




    def test_reating_four(self, setup):
        setup.get("http://127.0.0.1:5000")
        setup.find_element(By.XPATH, "(//img)[12]").click()
        setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("aya k")
        setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("Great movie")
        setup.find_element(By.CSS_SELECTOR, "label[title='Great']").click()
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert setup.find_element(By.XPATH, "//body/ol[2]/h2[15]").text == "4"
        log = self.getLogger()
        log.info("The rating will appear four")


    def test_reating_one(self, setup):
        setup.get("http://127.0.0.1:5000")

        setup.find_element(By.XPATH, "(//img)[12]").click()

        setup.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("bad movie")
        setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("good movie")
        setup.find_element(By.CSS_SELECTOR, "label[title='Bad']").click()
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        assert setup.find_element(By.XPATH, "//body/ol[2]/h2[16]").text == "1"
        log = self.getLogger()
        log.info("The raeting will appear one")



# def test_crossBrowser(crossBrowser):
#     print(crossBrowser)