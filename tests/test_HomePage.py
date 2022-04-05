import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("First Name is Rahul and Rekha")
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getradiobutton().click()
        self.selectOptionByText(homepage.dropdownmenu(),getData["gender"])
        homepage.submitbutton().click()
        message = homepage.getmessage().text
        assert "success"!!!!Thankyou!!!! in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return request.param
