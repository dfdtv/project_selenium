from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from base.base_class import Base

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    cart = '//div[@id="shopping_cart_container"]'


    #Getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.cart)))


    #Actions
    def click_product_1(self):
        self.get_product_1().click()
        print("Product 1 was added to cart")

    def click_enter_shopping_cart(self):
        self.get_cart().click()
        print("Shopping cart has opened")


    #Methods
    def add_product_to_cart(self):
        self.get_current_url()
        self.click_product_1()
        self.click_enter_shopping_cart()