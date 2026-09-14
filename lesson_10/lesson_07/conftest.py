import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    """Создаёт Chrome WebDriver и закрывает его после теста.

    Returns:
        Экземпляр Chrome WebDriver.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    """Создаёт Firefox WebDriver и закрывает его после теста.

    Returns:
        Экземпляр Firefox WebDriver.
    """
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
