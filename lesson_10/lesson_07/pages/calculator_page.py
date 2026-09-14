from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """Инициализирует страницу калькулятора.

        Args:
            driver: Экземпляр веб-драйвера.

        Returns:
            None.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        """Открывает страницу калькулятора.

        Returns:
            Экземпляр CalculatorPage.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """Устанавливает задержку калькулятора.

        Args:
            seconds: Задержка в секундах.

        Returns:
            Экземпляр CalculatorPage.
        """
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(seconds))
        return self

    def click_button(self, value: str) -> "CalculatorPage":
        """Нажимает кнопку калькулятора.

        Args:
            value: Текст кнопки.

        Returns:
            Экземпляр CalculatorPage.
        """
        self.driver.find_element(
            By.XPATH,
            f'//span[text()="{value}"]'
        ).click()
        return self

    def wait_for_result(
        self,
        expected_value: str,
        timeout: int = 50
    ) -> "CalculatorPage":
        """Ожидает появления результата.

        Args:
            expected_value: Ожидаемое значение результата.
            timeout: Максимальное время ожидания в секундах.

        Returns:
            Экземпляр CalculatorPage.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.screen,
                expected_value
            )
        )
        return self

    def get_result(self) -> str:
        """Возвращает результат калькулятора.

        Returns:
            Текст результата.
        """
        return self.driver.find_element(*self.screen).text
