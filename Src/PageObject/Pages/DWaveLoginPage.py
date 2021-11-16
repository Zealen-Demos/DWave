from selenium.webdriver.common.by import By


class DWaveLoginPage:
    URL = 'https://cloud.dwavesys.com/leap/login/'
    DWaveUsername = (By.XPATH, "//input[@name='username']")
    DWavePassword = (By.XPATH, "//input[@name='password']")
    DWaveLoginButton = (By.XPATH, "//input[@id='loginFormSubmit']")

    def __init__(self, driver):
        self.driver = driver

    def getUsername(self):
        return self.driver.find_element(*self.DWaveUsername)

    def getPassword(self):
        return self.driver.find_element(*self.DWavePassword)

    def getLoginButton(self):
        return self.driver.find_element(*self.DWaveLoginButton)
