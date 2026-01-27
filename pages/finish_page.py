from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from base.base_class import Base

class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Methods
    def finish(self):
        self.get_current_url()
        self.get_screenshot()