from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage
class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver



    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    checkout = (By.CSS_SELECTOR, "a[class*='btn']")
    purchase = (By.CSS_SELECTOR, "button[class*='btn-success']")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCheckoutbutton(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def purchasebutton(self):
        self.driver.find_element(*CheckoutPage.purchase).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage





