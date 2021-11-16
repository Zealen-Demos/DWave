import pytest
from selenium import webdriver
from time import sleep

from Src.PageObject.Pages.DWaveLoginPage import DWaveLoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="E:\Development\Python\DWave\chromedriver.exe")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_dwave_failed_login(browser):
    LoginPage = DWaveLoginPage(browser)
    browser.get(LoginPage.URL)
    LoginPage.getUsername().send_keys("fake_email@hotmail.com")
    LoginPage.getPassword().send_keys("123")
    LoginPage.getLoginButton().click()
    element = WebDriverWait(browser, 10).until(
        EC.url_matches('https://cloud.dwavesys.com/leap/')
    )
    assert browser.current_url != 'https://cloud.dwavesys.com/leap/'

def test_dwave_login(browser):
    LoginPage = DWaveLoginPage(browser)
    browser.get(LoginPage.URL)
    #Credentials should be moved to local configuration file
    LoginPage.getUsername().send_keys("********")
    LoginPage.getPassword().send_keys("********")
    LoginPage.getLoginButton().click()
    element = WebDriverWait(browser, 10).until(
        EC.url_matches('https://cloud.dwavesys.com/leap/')
    )
    assert browser.current_url == 'https://cloud.dwavesys.com/leap/'



