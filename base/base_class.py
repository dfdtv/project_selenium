

class Base:
    def __init__(self, driver):
        self.driver = driver

#Method Get Current URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current Url: {get_url}")