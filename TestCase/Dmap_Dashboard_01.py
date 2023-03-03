import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import validators

from PageObject.Pom import Loginpage


class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service(Loginpage.chrome)
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(Loginpage.URL)
        self.driver.find_element(By.CLASS_NAME, Loginpage.textbox_username_CSS).send_keys(Loginpage.username)
        time.sleep(1)
        self.driver.find_element(By.ID, Loginpage.textbox_password_id).send_keys(Loginpage.password)
        time.sleep(1)
        self.loginpage = Loginpage(self.driver)
        self.loginpage.clickLogin()
        time.sleep(2)

        # dashboard
        self.driver.find_element(By.XPATH, "//a[@title='Dashboard']").click()
        time.sleep(3)
        try:
            elements = self.driver.find_element(By.XPATH, "//span[normalize-space()='Dashboard']")
            print("Element found, You are logged in Dashboard : Using Try & Exception")
        except NoSuchElementException:
            print("Element not found, Since you Are not Logged in")
        # Dashboard_VALID
        valid = validators.url('https://admetrics-dev.tibilprojects.com/#/dashboard')
        print(valid)
        if True == valid:
            print("You are in Dashboard: Using URL Validation")
        else:
            print("You are not in Dashboard")
        time.sleep(3)

        # # Dashboard verification
        #     # google analytics
        #     Dashboard_display = self.driver.find_element(By.XPATH, "//span[normalize-space()='Google Analytics']")
        #     print("Element Found : Google Analytics", Dashboard_display.is_displayed())
        #     time.sleep(5)
        #     if Dashboard_display.is_displayed() == True:
        #         assert True
        #     else:
        #         print("Element Not Found : Verify the login", Dashboard_display.is_displayed())
        #      # Google Ads
        #     Dashboard_display = self.driver.find_element(By.XPATH, "//span[normalize-space()='Google Ads']")
        #     print("Element Found : Google Ads", Dashboard_display.is_displayed())
        #     time.sleep(5)
        #     if Dashboard_display.is_displayed() == True:
        #         assert True
        #     else:
        #         print("Element Not Found : Verify the login", Dashboard_display.is_displayed())
        #
        #
        #     # Facebook
        #     Dashboard_display = self.driver.find_element(By.XPATH, "//span[normalize-space()='Facebook']")
        #     print("Element Found : Facebook", Dashboard_display.is_displayed())
        #     time.sleep(5)
        #     if Dashboard_display.is_displayed() == True:
        #         assert True
        #     else:
        #         print("Element Not Found : Verify the login", Dashboard_display.is_displayed())
        #
        #
        #     # LinkedIn
        #     Dashboard_display = self.driver.find_element(By.XPATH, "//span[normalize-space()='Linkedin']")
        #     print("Element Found : LinkedIN", Dashboard_display.is_displayed())
        #     time.sleep(5)
        #     if Dashboard_display.is_displayed() == True:
        #         assert True
        #     else:
        #         print("Element Not Found : Verify the login", Dashboard_display.is_displayed())
        #
        #
        #     # Focus On
        #     Dashboard_display = self.driver.find_element(By.XPATH, "//span[normalize-space()='Focus On']")
        #     print("Element Found : Focus On", Dashboard_display.is_displayed())
        #     time.sleep(5)
        #     if Dashboard_display.is_displayed() == True:
        #         assert True
        #     else:
        #         print("Element Not Found : Verify the login", Dashboard_display.is_displayed())

        # Dashboard elements
        # self.driver.find_element(By.XPATH, "//a[@title='Dashboard']").click()
        # time.sleep(2)
        # try:
        #     elements = self.driver.find_element(By.XPATH, "//span[normalize-space()='Dashboard']")
        #     print("Element found, You are logged in Dashboard : Using Try & Exception")
        # except NoSuchElementException:
        #     print("Element not found, Since you Are not Logged in")
        # # Dashboard_VALID
        # valid = validators.url('https://admetrics-dev.tibilprojects.com/#/dashboard')
        # print(valid)
        # if True == valid:
        #     print("You are in Dashboard: Using URL Validation")
        # else:
        #     print("You are not in Dashboard")
        # # full Screen
        # self.driver.find_element(By.XPATH, "//button[2]//*[name()='svg']").click()
        # time.sleep(2)
        # Overall Traffic Option
        self.driver.find_element(By.XPATH, "//p[normalize-space()='Overall Traffic']").click()
        time.sleep(2)
        try:
            elements = self.driver.find_element(By.XPATH, "//p[normalize-space()='Overall Traffic']")
            print("Element found, Have selected Overall Traffic")
        except NoSuchElementException:
            print("Element not found")
        time.sleep(2)
        # # Organic Traffic Option
        # self.driver.find_element(By.XPATH, "//p[normalize-space()='Organic Traffic']").click()
        # time.sleep(2)
        # try:
        #     elements = self.driver.find_element(By.XPATH, "//p[normalize-space()='Organic Traffic']")
        #     print("Element found, Have selected Organic Traffic")
        # except NoSuchElementException:
        #     print("Element not found")
        # time.sleep(2)
        # # Sessions Option
        # self.driver.find_element(By.XPATH, "//p[normalize-space()='Sessions']").click()
        # try:
        #     elements = self.driver.find_element(By.XPATH, "//p[normalize-space()='Sessions']")
        #     print("Element found, Have selected Sessions")
        # except NoSuchElementException:
        #     print("Element not found")
        # time.sleep(2)
        # # Page Views Option
        # self.driver.find_element(By.XPATH, "//p[normalize-space()='Page Views']").click()
        # try:
        #     elements = self.driver.find_element(By.XPATH, "//p[normalize-space()='Page Views']")
        #     print("Element found, Have selected Page Views")
        # except NoSuchElementException:
        #     print("Element not found")
        # time.sleep(2)
        # # Focus On
        # self.driver.find_element(By.XPATH, "//span[normalize-space()='Focus On']").click()
        # try:
        #     elements = self.driver.find_element(By.XPATH, "//span[normalize-space()='Focus On']")
        #     print("Element found, Have selected Focus On ")
        # except NoSuchElementException:
        #     print("Element not found")
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//input[@value='custom']").click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Apply']").click()
        # try:
        #     elements = self.driver.find_element(By.XPATH, "//span[normalize-space()='Focus On']")
        #     print("Element found, Focus on Is applied")
        # except NoSuchElementException:
        #     print("Element not found")
        # time.sleep(2)

        self.driver.close()
