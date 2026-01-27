from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from base.base_class import Base

class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    finish = '//button[@id="finish"]'


    #Getters
    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.finish)))



    #Actions
    def click_finish_button(self):
        self.get_finish_button().click()
        print("Finish button has been clicked")


    #Methods
    def payment(self):
        self.click_finish_button()