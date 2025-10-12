from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()

    try:
        calc_page = CalculatorPage(driver)

        base_url = "https://bonigarcia.dev/selenium-webdriver-java/"
        url = base_url + "slow-calculator.html"
        calc_page.open(url)

        calc_page.set_delay(45)

        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

        calc_page.wait_for_result("15")

        result = calc_page.get_result()
        assert result == "15", f"Ожидался результат 15, но получен: {result}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()
