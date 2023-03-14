
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

import pytest


@pytest.fixture(params=["chrome", "edge"])
def setup(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        service = ChromeService("../chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif request.param == "edge":
        edge_options = EdgeOptions()
        edge_options.add_experimental_option("detach", True)
        service = EdgeService("../edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=service, options=edge_options)
    else:
        raise ValueError("Invalid browser specified. Must be 'chrome' or 'edge'.")

    driver.maximize_window()
    yield driver
    driver.quit()





# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
# import pytest
#
# @pytest.fixture()
# def setup():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#     service_obj = Service("../chromedriver_win32/chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#     driver.maximize_window()
#     return driver
#
# @pytest.fixture(params=["Chrome", "Edge"])
# def crossBrowser(request):
#     return request.param
#
#