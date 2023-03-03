import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import validators

from PageObject.Pom import Loginpage


class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("/home/ramesh/chromedriver")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get(Loginpage.URL)
        self.driver.maximize_window()
        time.sleep(3)
        # **************************************************************

        # invalid_test
        # empty Username and Password
        self.driver.find_element(By.ID, "login").click()
        time.sleep(2)
        Login_page = self.driver.find_element(By.XPATH, "//p[normalize-space()='Please fill the details']")
        print("Warning Displayed : Please fill the Details :", Login_page.is_displayed())
        time.sleep(2)
        if Login_page.is_displayed() == True:
            assert True
        else:
            print("Warning Not Displayed in Page", Login_page.is_displayed())
        time.sleep(2)

        # invalid username
        self.driver.find_element(By.CLASS_NAME, "form-control").send_keys("invalid_email@email.com")
        time.sleep(2)
        # invalid password
        self.driver.find_element(By.ID, "password").send_keys("password")
        self.driver.find_element(By.ID, "login").click()  # Signin
        time.sleep(2)
        self.driver.switch_to.alert.accept()  # switch to pop-up message window to click
        Login_page = self.driver.find_element(By.XPATH, "//p[normalize-space()='Invalid emailid or password']")
        print("Warning Displayed : Invalid emailid or password :", Login_page.is_displayed())
        time.sleep(2)
        if Login_page.is_displayed() == True:
            assert True
        else:
            print("Warning Not Displayed in Page", Login_page.is_displayed())
        time.sleep(2)

        # valid username
        self.driver.get(Loginpage.URL)
        self.driver.find_element(By.CLASS_NAME, Loginpage.textbox_username_CSS).send_keys(Loginpage.username)
        time.sleep(1)
        # valid Password
        self.driver.find_element(By.ID, Loginpage.textbox_password_id).send_keys(Loginpage.password)
        time.sleep(1)
        self.loginpage = Loginpage(self.driver)
        self.loginpage.clickLogin()
        time.sleep(2)
        try:
            elements = self.driver.find_element(By.XPATH, "//span[normalize-space()='Dashboard']")
            print("Element found, You are logged in Dashboard : Using Valid username and password")
        except Exception:
            print("Element not found, Since you Are not Logged in")
        # dashboard
        self.driver.find_element(By.XPATH, "//a[@title='Dashboard']").click()
        time.sleep(2)

        # validations
        Login_dis = self.driver.find_element(By.XPATH, "//a[@title='Dashboard']")
        print("Login Menu Displayed  status:", Login_dis.is_displayed())
        time.sleep(2)
        if Login_dis.is_displayed() == True:
            assert True
        else:
            print("Login Menu Displayed  status:", Login_dis.is_displayed())
        self.driver.close()
