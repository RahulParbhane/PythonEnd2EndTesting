from selenium.webdriver.common.by import By
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("getting all the card Titles")
        products = checkoutpage.getCardTitles()
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()

        checkoutpage.getCheckoutbutton().click()
        confirmpage = checkoutpage.purchasebutton()
        log.info("Entering country name as ind")
        confirmpage.getCountryValue().send_keys("ind")
        self.verifylinkPresence("India")
        confirmpage.getCountryName().click()
        confirmpage.getPurchaseButton().click()
        confirmpage.getcheckbutton().click()
        successText = confirmpage.getalerttext().text
        log.info("Text Received from application is "+successText)
        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")