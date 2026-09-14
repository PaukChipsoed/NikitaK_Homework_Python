from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if TYPE_CHECKING:
    from pages.inventory_page import InventoryPage


class LoginPage:
    def __init__(self, driver) -> None:
        """Инициализирует страницу авторизации.

        Args:
            driver: Экземпляр веб-драйвера.

        Returns:
            None.
        """
        self.driver = driver

    def open(self) -> "LoginPage":
        """Открывает страницу авторизации.

        Returns:
            Экземпляр LoginPage.
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(
        self,
        username: str,
        password: str
    ) -> "InventoryPage":
        """Авторизует пользователя.

        Args:
            username: Имя пользователя.
            password: Пароль пользователя.

        Returns:
            Экземпляр InventoryPage.
        """
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
