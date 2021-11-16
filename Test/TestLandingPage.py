import pytest
from selenium import webdriver
from time import sleep

from Src.PageObject.Pages.DWaveLoginPage import DWaveLoginPage
from Src.PageObject.Pages.DWaveLandingPage import DWaveLandingPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="E:\Development\Python\DWave\chromedriver.exe")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def login(browser):
    LoginPage = DWaveLoginPage(browser)
    browser.get(LoginPage.URL)
    LoginPage.getUsername().send_keys("fall_back_up@hotmail.com")
    LoginPage.getPassword().send_keys("Dylan*Jack123")
    LoginPage.getLoginButton().click()
    element = WebDriverWait(browser, 10).until(
        EC.url_matches('https://cloud.dwavesys.com/leap/')
    )
    return browser


def test_dwave_verify_account_info(login):
    LandingPage = DWaveLandingPage(login)

    assert login.current_url == 'https://cloud.dwavesys.com/leap/'
    assert LandingPage.getFullname().text == 'Dylan Jack'
    assert LandingPage.getAccountType().text == 'Trial Plan'
    assert LandingPage.getPlanExpiry().text == 'December 16, 2021 (UTC)'



