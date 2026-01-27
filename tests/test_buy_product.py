import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_pages import Payment_page


def test_buy_product():
    driver = webdriver.Chrome()
    print("Starting test")

    login = Login_page(driver)
    mp = Main_page(driver)
    cp = Cart_page(driver)
    cip = Client_information_page(driver)
    p = Payment_page(driver)
    f = Finish_page(driver)

    login.authorization()
    mp.add_product_to_cart()
    cp.product_confirmation()
    cip.input_client_information()
    p.payment()
    f.finish()
