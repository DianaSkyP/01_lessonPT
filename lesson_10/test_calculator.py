import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.feature("Calculator Tests")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Calculator Operations")
@allure.description("Test calculator functionality with delay and arithmetic")
def test_calculator():
    driver = webdriver.Chrome()

    try:
        with allure.step("Initialize calculator page"):
            calc_page = CalculatorPage(driver)

        with allure.step("Open calculator URL"):
            base_url = "https://bonigarcia.dev/selenium-webdriver-java/"
            url = base_url + "slow-calculator.html"
            calc_page.open(url)

        with allure.step("Set calculator delay to 45 seconds"):
            calc_page.set_delay(45)

        with allure.step("Perform calculation: 7 + 8"):
            calc_page.click_button("7")
            calc_page.click_button("+")
            calc_page.click_button("8")
            calc_page.click_button("=")

        with allure.step("Wait for result and verify"):
            calc_page.wait_for_result("15")
            result = calc_page.get_result()

            with allure.step("Verify calculation result"):
                assert result == "15", (
                    f"Ожидался результат 15, получен: {result}"
                )

    finally:
        with allure.step("Close browser"):
            driver.quit()


if __name__ == "__main__":
    test_calculator()
