

class Base:
    def __init__(self, driver):
        self.driver = driver

#Method Get Current URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current Url: {get_url}")

#Method assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Word is Correct")
