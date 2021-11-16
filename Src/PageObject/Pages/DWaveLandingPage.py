from selenium.webdriver.common.by import By


class DWaveLandingPage:
    FullName = (By.XPATH, "//div[contains(@class, 'full-name')]")
    AccountType = (By.XPATH, "(.//div[contains(@class, 'account-card-section')]//div[contains(@class, 'body-text')])[1]")
    PlanExpiry = (By.XPATH, "(.//div[contains(@class, 'account-card-section')]//div[contains(@class, 'body-text')])[2]")

    def __init__(self, driver):
        self.driver = driver

    def getFullname(self):
        return self.driver.find_element(*self.FullName)

    def getAccountType(self):
        return self.driver.find_element(*self.AccountType)

    def getPlanExpiry(self):
        return self.driver.find_element(*self.PlanExpiry)
