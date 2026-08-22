from pages.login_page import LoginPage


def test_shop(firefox_driver):
    login_page = LoginPage(firefox_driver)

    login_page.open()

    inventory_page = login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page.add_to_cart(
        "sauce-labs-backpack"
    )

    inventory_page.add_to_cart(
        "sauce-labs-bolt-t-shirt"
    )

    inventory_page.add_to_cart(
        "sauce-labs-onesie"
    )

    cart_page = inventory_page.go_to_cart()

    checkout_page = cart_page.proceed_to_checkout()

    checkout_page.fill_form(
        "Иван",
        "Иванов",
        "123456"
    )

    checkout_page.continue_checkout()

    total = checkout_page.get_total()

    assert total == "58.29", (
        f"Ожидалось $58.29, получено ${total}"
    )
