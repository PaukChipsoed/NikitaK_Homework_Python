from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id):
        self.driver.find_element(
            By.ID,
            f"add-to-cart-{product_id}"
        ).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            '[data-test="shopping-cart-link"]'
        ).click()

        from pages.cart_page import CartPage
        return CartPage(self.driver)
