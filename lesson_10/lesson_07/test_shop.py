import allure

from pages.login_page import LoginPage


@allure.title("Покупка трех товаров")
@allure.description(
    "Проверка покупки трех товаров через корзину."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(firefox_driver):
    login_page = LoginPage(firefox_driver)

    with allure.step("Открыть магазин"):
        login_page.open()

    with allure.step("Авторизоваться"):
        inventory_page = login_page.login(
            "standard_user",
            "secret_sauce"
        )

    with allure.step("Добавить товары в корзину"):
        inventory_page.add_to_cart(
            "sauce-labs-backpack"
        )
        inventory_page.add_to_cart(
            "sauce-labs-bolt-t-shirt"
        )
        inventory_page.add_to_cart(
            "sauce-labs-onesie"
        )

    with allure.step("Перейти в корзину"):
        cart_page = inventory_page.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        checkout_page = cart_page.proceed_to_checkout()

    with allure.step("Заполнить данные покупателя"):
        checkout_page.fill_form(
            "Иван",
            "Иванов",
            "123456"
        )

    with allure.step("Продолжить оформление заказа"):
        checkout_page.continue_checkout()

    with allure.step("Проверить итоговую стоимость"):
        total = checkout_page.get_total()

        assert total == "58.29", (
            f"Ожидалось $58.29, получено ${total}"
        )
