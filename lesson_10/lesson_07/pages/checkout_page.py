from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver) -> None:
        """Инициализирует страницу оформления заказа.

        Args:
            driver: Экземпляр веб-драйвера.

        Returns:
            None.
        """
        self.driver = driver

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> "CheckoutPage":
        """Заполняет форму оформления заказа.

        Args:
            first_name: Имя покупателя.
            last_name: Фамилия покупателя.
            postal_code: Почтовый индекс.

        Returns:
            Экземпляр CheckoutPage.
        """
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

    def continue_checkout(self) -> "CheckoutPage":
        """Продолжает оформление заказа.

        Returns:
            Экземпляр CheckoutPage.
        """
        self.driver.find_element(
            By.ID, "continue"
        ).click()
        return self

    def get_total(self) -> str:
        """Получает итоговую стоимость заказа.

        Returns:
            Итоговая стоимость без текста Total и символа $.
        """
        total_text = self.driver.find_element(
            By.CSS_SELECTOR,
            '[data-test="total-label"]'
        ).text

        return total_text.replace("Total: $", "")
