import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_buy_product():
    driver = webdriver.Chrome()
    print("Starting test")

    login = Login_page(driver)
    mp = Main_page(driver)
    cp = Cart_page(driver)
    login.authorization()
    mp.add_product_to_cart()
    cp.product_confirmation()

    # enter_shopping_cart = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable(('xpath', '//div[id="shopping_cart_container"]')))
    # enter_shopping_cart.click()
    # print("Click Enter Shopping Cart")
