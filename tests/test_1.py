from selenium import webdriver
from pages.login_page import Login_page

users_list = ["standart_user", "locked_out_user", "problem_user", "performance_glitch_user"]

class Test_1:
    def test_login(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()

        login = Login_page(driver)
        login.authorization(login_name= users_list[0], login_password="secret_sauce")
test = Test_1()
test.test_login()