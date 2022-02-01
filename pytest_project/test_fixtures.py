from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import pytest

#Driver variable
driver = None

#fixture decorators
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------setup--------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    #is used to return from a function without destroying the states of its local variable
    yield

    print("---------teardown----------")
    driver.quit()

"""
if we don't want to use fixture name as an arguement inside the method
then we can directly declare an annotation above the required function 

"""
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == 'Google'

@pytest.mark.usefixtures()
def test_google_url(init_driver):
    assert driver.current_url == 'https://www.google.com/?gws_rd=ssl'

