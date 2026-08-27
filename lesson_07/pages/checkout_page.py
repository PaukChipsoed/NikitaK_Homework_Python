from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(
            By.ID, "first-name"
        ).send_keys(first_name)

        self.driver.find_element(
            By.ID, "last-name"
        ).send_keys(last_name)

        self.driver.find_element(
            By.ID, "postal-code"
        ).send_keys(postal_code)

        return self

    def continue_checkout(self):
        self.driver.find_element(
            By.ID, "continue"
        ).click()
        return self

    def get_total(self):
        total_text = self.driver.find_element(
            By.CSS_SELECTOR,
            '[data-test="total-label"]'
        ).text

        return total_text.replace("Total: $", "")
