from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)  
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    total_text = driver.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text
    total_value = total_text.replace("Total: $", "")

    assert total_value == "58.29", f"Ожидалось $58.29, получено ${total_value}"

    driver.quit()