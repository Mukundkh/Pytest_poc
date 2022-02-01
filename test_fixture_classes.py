from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
"""
    pytest fixtures with the 
    class scope
"""
@pytest.fixture(scope='class')
def init_chrome_driver(request):
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = chrome_driver
    #tear down method with the help of yield keyword
    yield
    chrome_driver.close()
    

#Fixture for firefox class
@pytest.fixture(scope='class')
def init_firefox_driver(request):
    firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = firefox_driver
    #tear down method with the help of yield keyword
    yield
    firefox_driver.close()

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test():
    pass

class Test_Google_Chrome(Base_Chrome_Test):

    def test_google_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == 'Google'

#another one for firefox class
@pytest.mark.usefixtures("init_firefox_driver")
class Base_FireFox_Test():
    pass

class Test_Google_FireFox(Base_FireFox_Test):

    def test_google_title_firefox(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == 'Google'