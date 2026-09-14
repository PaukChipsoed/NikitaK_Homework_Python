from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver) -> None:
        """Инициализирует страницу товаров.

        Args:
            driver: Экземпляр веб-драйвера.

        Returns:
            None.
        """
        self.driver = driver

    def add_to_cart(self, product_id: str) -> "InventoryPage":
        """Добавляет товар в корзину.

        Args:
            product_id: Идентификатор товара.

        Returns:
            Экземпляр InventoryPage.
        """
        self.driver.find_element(
            By.ID,
            f"add-to-cart-{product_id}"
        ).click()
        return self

    def go_to_cart(self):
        """Переходит в корзину.

        Returns:
            Экземпляр CartPage.
        """
        self.driver.find_element(
            By.CSS_SELECTOR,
            '[data-test="shopping-cart-link"]'
        ).click()

        from pages.cart_page import CartPage
        return CartPage(self.driver)
