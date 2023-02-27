import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options =Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("homedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.get("http://127.0.0.1:5000")


# TEST 1:  Delet button- delet movie from  the home page & database

before_delete= driver.find_elements(By.XPATH,"//div/a/img")
driver.find_element(By.XPATH, "//body[1]/div[1]/div[12]/a[1]").click()
# driver.get("http://127.0.0.1:5000/movie_info/11")
driver.find_element(By.XPATH, "//a[normalize-space()='Delete']").click()
after_delete = driver.find_elements(By.XPATH,"//div/a/img")
assert len(after_delete) < len(before_delete), "the movie is not delete"

print("delete movie!")





# TEST 2: ALTER TEST to test if the user can update the title movie.(alter button)

driver.find_element(By.XPATH, "(//img)[12]").click()

driver.find_element(By.XPATH, "//a[normalize-space()='alter']").click()
driver.find_element(By.XPATH, "//input[@name='movie_title']").send_keys("the dark")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
assert driver.find_element(By.CSS_SELECTOR, "h1").text == "the dark"
print("the title update")





# TEST 3:  ADD movie

before_add = driver.find_elements(By.XPATH,"//div/a/img")
driver.find_element(By.XPATH, "//a[contains(.,'Add movies')]").click()
driver.find_element(By.NAME, 'filename').send_keys("C:/Users/Administrator/Desktop/abb.jpg")
driver.find_element(By.NAME,'movie_title').send_keys("aya")
driver.find_element(By.NAME, 'description').send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
driver.find_element(By.NAME,'director').send_keys("kaabyia")
driver.find_element(By.NAME, 'actor').send_keys("aya, jood, ali")
driver.find_element(By.NAME,'release_year').send_keys(2022)
# define the HTML code for the iframe
# inject the HTML code for the iframe into the element
iframe_html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/1NJO0jxBtMo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
driver.find_element(By.NAME, 'video').send_keys(iframe_html)
driver.find_element(By.XPATH, "//button[normalize-space()='ADD']").click()
after_add = driver.find_elements(By.XPATH,"//div/a/img")
assert len(after_add) > len(before_add), "the movie is not add"
print("the movie addad!")



# TEST 4:  PASS TO INFO MOVIE win click on the poster the movie in the home page

driver.find_element(By.XPATH, "//body/div[@class='bg']/div[1]/a[1]").click()
assert driver.current_url == "http://127.0.0.1:5000/movie_info/1"
print("passed!")







# TEST 5 :LOGO BUTTON - can back to home page

driver.find_element(By.XPATH, "(//img)[12]").click()
driver.find_element(By.CSS_SELECTOR, "img[alt='logo']").click()
assert driver.current_url == "http://127.0.0.1:5000/"
print("passed!")







# TEST 6:  SEARCH ABOuT TITLE MOVIE FROM HOMEPAGE

driver.find_element(By.XPATH, "//input[@id='search ']").send_keys("Toy story")
driver.find_element(By.CSS_SELECTOR, "#submit").click()
assert driver.find_element(By.XPATH, "//h1[normalize-space()='Toy Story']").text == "Toy Story"
print("the search pass")







# TEST 7: rating 5-starts

driver.find_element(By.XPATH, "(//img)[12]").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("aya")
driver.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("Awesome")
driver.find_element(By.CSS_SELECTOR, "label[title='Awesome']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("aya k")
driver.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("Great movie")
driver.find_element(By.CSS_SELECTOR, "label[title='Great']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("jood")
driver.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("Very good movie")
driver.find_element(By.CSS_SELECTOR, "label[title='Very good']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ali")
driver.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("good movie")
driver.find_element(By.CSS_SELECTOR, "label[title='Good']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("bad movie")
driver.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("good movie")
driver.find_element(By.CSS_SELECTOR, "label[title='Bad']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()






# TEST 8 : reviwe comment if the user can to write commint.

driver.find_element(By.XPATH, "(//img)[12]").click()
before_new_comment = driver.find_elements(By.XPATH,"(//li[contains(text(),'Name:')])")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Talia")
driver.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("Awesome")
driver.find_element(By.CSS_SELECTOR, "label[title='Awesome']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
after_new_comment = driver.find_elements(By.XPATH,"(//li[contains(text(),'Name:')])")
assert len(after_new_comment) > len(before_new_comment), "the comment is not add"
print("the comment addad!")







# TEST 9: go to top page
#
driver.find_element(By.XPATH, "(//img)[12]").click()
driver.find_element(By.CSS_SELECTOR, "div[class='button']").click()

# scroll to the top of the page using JavaScript
driver.execute_script("window.scrollTo(0, 0);")
# verify that the page has scrolled to the top by checking the scroll position
scroll_position = driver.execute_script("return window.pageYOffset;")
assert scroll_position == 0
print("go to the top page")








# TEST 10:  SEARCH ABOuT TITLE MOVIE not foind FROM HOMEPAGE

driver.find_element(By.XPATH, "//input[@id='search ']").send_keys("hi")
driver.find_element(By.CSS_SELECTOR, "#submit").click()
assert driver.find_element(By.CSS_SELECTOR, "div[id='myTopnav'] h1").text == "Nothing found"
print("the search nothing found pass")


