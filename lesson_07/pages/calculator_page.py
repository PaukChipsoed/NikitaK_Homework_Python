from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        return self

    def set_delay(self, seconds):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(seconds))
        return self

    def click_button(self, value):
        self.driver.find_element(
            By.XPATH,
            f'//span[text()="{value}"]'
        ).click()
        return self

    def wait_for_result(self, expected_value, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.screen,
                str(expected_value)
            )
        )
        return self

    def get_result(self):
        return self.driver.find_element(*self.screen).text
