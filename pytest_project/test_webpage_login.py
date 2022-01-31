from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import datetime
def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(20)
    driver.get('http://www.gmail.com')
    assert driver.title == 'Gmail'
    driver.quit()
     
def test_instagram():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(20)
    driver.get('http://www.instagram.com')
    assert driver.title == 'Instagram'
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(20)
    driver.get('http://www.facebook.com')
    assert driver.title == 'Facebook – log in or sign up'
    driver.quit()

def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(20)
    driver.get('http://www.rediff.com')
    assert driver.title == 'Rediff.com: News | Rediffmail | Stock Quotes | Shopping'
    driver.quit()
     