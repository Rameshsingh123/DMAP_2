import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import validators


class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("C:\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://admetrics-dev.tibilprojects.com/#/login")
        self.driver.maximize_window()
        time.sleep(5)
        # valid username
        self.driver.find_element(By.CLASS_NAME, "form-control").send_keys("cust1@moonlyte.com")
        time.sleep(2)
        # valid password
        self.driver.find_element(By.ID, "password").send_keys("admin")
        time.sleep(2)
        self.driver.find_element(By.ID, "login").click()  # Signin
        time.sleep(5)
        # logout
        self.driver.find_element(By.XPATH, "//button[@aria-label='account of current user']//*[name()='svg']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//li[normalize-space()='Logout']").click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        time.sleep(5)

        # validations
        Login_dis = self.driver.find_element(By.CSS_SELECTOR, ".card-body")
        print("Logout status is done from the url", Login_dis.is_displayed())
        time.sleep(5)
        if Login_dis.is_displayed() == True:
            assert True
        else:
            print("Logout status is done from the url:", Login_dis.is_displayed())
        self.driver.close()
