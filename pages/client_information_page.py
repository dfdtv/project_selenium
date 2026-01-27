from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from faker import Faker
from base.base_class import Base

fake = Faker('en_US')

class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//input[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'

    #Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.continue_button)))

    #Actions
    def input_first_name(self):
        first_name = fake.first_name()
        self.get_first_name().send_keys(first_name)
        print("First Name has been inputted")

    def input_last_name(self):
        last_name = fake.last_name()
        self.get_last_name().send_keys(last_name)
        print("Last Name has been inputted")

    def input_postal_code(self):
        postal_code = fake.postcode()
        self.get_postal_code().send_keys(postal_code)
        print("Postal Code has been inputted")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Continue button has been clicked")


    #Methods
    def input_client_information(self):
        self.input_first_name()
        self.input_last_name()
        self.input_postal_code()
        self.click_continue_button()