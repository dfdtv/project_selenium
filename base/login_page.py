from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

base_url = 'https://www.saucedemo.com'
login_standart = 'standard_user'
password_all = 'secret_sauce'

class Login_page:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):

        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('id', 'user-name')))
        user_name.send_keys(login_name)
        print("Логин введен")

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('id', 'password')))
        password.send_keys(login_password)
        password.send_keys(Keys.ENTER)
        print("Вход выполнен")

