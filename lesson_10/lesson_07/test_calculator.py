import allure

from pages.calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description(
    "Проверка сложения 7 и 8 с задержкой 45 секунд."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(chrome_driver):
    calc = CalculatorPage(chrome_driver)

    with allure.step("Открыть страницу калькулятора"):
        calc.open()

    with allure.step("Установить задержку 45 секунд"):
        calc.set_delay(45)

    with allure.step("Нажать 7"):
        calc.click_button("7")

    with allure.step("Нажать +"):
        calc.click_button("+")

    with allure.step("Нажать 8"):
        calc.click_button("8")

    with allure.step("Нажать ="):
        calc.click_button("=")

    with allure.step("Дождаться результата 15"):
        calc.wait_for_result("15", 50)

    with allure.step("Проверить результат"):
        assert calc.get_result() == "15"
