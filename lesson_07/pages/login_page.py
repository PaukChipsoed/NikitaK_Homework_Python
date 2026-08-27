from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        ).send_keys(username)

        self.driver.find_element(
            By.ID, "password"
        ).send_keys(password)

        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "login-button")
            )
        ).click()

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
