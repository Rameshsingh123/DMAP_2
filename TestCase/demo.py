from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time

from PageObject.Pom import Loginpage


class TestLogin:

    def test_login(self):
        self.serv_obj = Service(Loginpage.chrome)
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.maximize_window()
        self.driver.get(Loginpage.URL)
        self.driver.find_element(By.CLASS_NAME, Loginpage.textbox_username_CSS).send_keys(Loginpage.username)
        time.sleep(1)
        self.driver.find_element(By.ID, Loginpage.textbox_password_id).send_keys(Loginpage.password)
        # driver.implicitly_wait(100)
        time.sleep(1)
        self.loginpage = Loginpage(self.driver)
        self.loginpage.clickLogin()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//p[normalize-space()='Overall Traffic']").click()
        time.sleep(2)
        try:
            elements = self.driver.find_element(By.XPATH, "//p[normalize-space()='Overall Traffic']")
            print("Element found, Have selected Overall Traffic")
        except NoSuchElementException:
            print("Element not found")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/main/div[3]/div/div[3]/div/div[1]/div/div/div[2]/div[1]/svg/g[2]/path[48]").click()
        time.sleep(100)