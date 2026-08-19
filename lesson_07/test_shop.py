from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return InventoryPage(self.driver)


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id):
        self.driver.find_element(By.ID, f"add-to-cart-{product_id}").click()
        return self

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        return CartPage(self.driver)


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        return CheckoutPage(self.driver)


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        return self

    def continue_checkout(self):
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total(self):
        total_text = self.driver.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text
        return total_text.replace("Total: $", "")


def test_shop():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    login_page = LoginPage(driver)
    login_page.open()
    inventory_page = login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart("sauce-labs-onesie")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.proceed_to_checkout()

    checkout_page.fill_form("Иван", "Иванов", "123456")
    checkout_page.continue_checkout()

    total = checkout_page.get_total()
    assert total == "58.29", f"Ожидалось $58.29, получено ${total}"

    driver.quit()


if __name__ == "__main__":
    test_shop()