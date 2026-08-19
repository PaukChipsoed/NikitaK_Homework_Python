from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, seconds):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(seconds))
        return self

    def click_button(self, value):
        self.driver.find_element(By.XPATH, f'//span[text()="{value}"]').click()
        return self

    def wait_for_result(self, expected_value, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, str(expected_value))
        )
        return self

    def get_result(self):
        return self.driver.find_element(*self.screen).text


def test_calculator():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    calc = CalculatorPage(driver)
    calc.open()
    calc.set_delay(45)
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")
    calc.wait_for_result("15", 50)

    assert calc.get_result() == "15"

    driver.quit()


if __name__ == "__main__":
    test_calculator()