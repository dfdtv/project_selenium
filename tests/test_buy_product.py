import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page

users_list = ["standart_user", "locked_out_user", "problem_user", "performance_glitch_user"]

def test_login(self):
    driver = webdriver.Chrome()
    print("Starting test")

    enter_shopping_cart = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(('xpath', '//div[id="shopping_cart_container"]')))
    enter_shopping_cart.click()
    print("Click Enter Shopping Cart")
