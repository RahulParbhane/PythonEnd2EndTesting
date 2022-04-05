from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    radio = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getradiobutton(self):
        return self.driver.find_element(*HomePage.radio)

    def dropdownmenu(self):
        return self.driver.find_element(*HomePage.dropdown)

    def submitbutton(self):
        return self.driver.find_element(*HomePage.submit)

    def getmessage(self):
        return self.driver.find_element(*HomePage.message)