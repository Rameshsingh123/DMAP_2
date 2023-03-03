from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


class Loginpage:
    # locators

    chrome = "/home/ramesh/chromedriver"
    URL = "https://admetrics-dev.tibilprojects.com/#/login"
    username = "cust1@moonlyte.com"
    password = "admin"
    textbox_username_CSS = "form-control"
    textbox_password_id = "password"
    button_login_id = "login"

    # element_signout_Xpath = "//i[@class='fa fa-sign-out']"
    # constructor
    def __init__(self, driver):
        self.driver = driver

    # username

    def setUserName(self, username):
        usernametxt = self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_CSS)
        usernametxt.send_keys(username)

    #  password
    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.ID, self.textbox_password_id)
        passwordtxt.send_keys(password)

    # LOGIN
    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()
#

#     def signout(self):
#          action = ActionChains(self.driver)
#          element = self.driver.find_element(By.XPATH,self.imgxpath)
#          action.move_to_element(element)
#          action.perform()
# # click signout
#          self.driver.find_element(By.XPATH,self.element_signout_Xpath).click()
