from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    country = (By.ID, "country")
    countryname = (By.LINK_TEXT, "India")
    purchasebutton = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    check = (By.CSS_SELECTOR, "input[value='Purchase']")
    alerttext = (By.CSS_SELECTOR, "div[class*='alert']")

    def getCountryValue(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.countryname)


    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchasebutton)

    def getcheckbutton(self):
        return self.driver.find_element(*ConfirmPage.check)

    def getalerttext(self):
        return self.driver.find_element(*ConfirmPage.alerttext)