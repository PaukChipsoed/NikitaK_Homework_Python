from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver) -> None:
        """Инициализирует страницу корзины.

        Args:
            driver: Экземпляр веб-драйвера.

        Returns:
            None.
        """
        self.driver = driver

    def proceed_to_checkout(self):
        """Переходит к оформлению заказа.

        Returns:
            Экземпляр CheckoutPage.
        """
        self.driver.find_element(
            By.ID, "checkout"
        ).click()

        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)
