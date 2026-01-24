from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from base.base_class import Base

class Login_page(Base):
    base_url = 'https://www.saucedemo.com'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    user_name = '//input[@id="user-name"]'
    password = '//input[@id="password"]'
    login_btn = '//input[@id="login-button"]'

    #Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.user_name)))


    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.password)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.login_btn)))


    #Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name successfully")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password successfully")

    def click_login_btn(self):
        self.get_login_btn().click()
        print("Click login button successfully")



    #Methods
    def authorization(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_btn()