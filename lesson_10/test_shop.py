import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage


@allure.feature("E-commerce Tests")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Complete Purchase Flow")
@allure.description("Test e-commerce purchase flow: login, add products")
def test_shop_purchase():
    with allure.step("Configure Chrome options"):
        chrome_options = Options()
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-password-manager-reauth")
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })

    driver = webdriver.Chrome(options=chrome_options)

    try:
        with allure.step("Initialize page objects"):
            login_page = LoginPage(driver)
            main_page = MainPage(driver)
            cart_page = CartPage(driver)
            checkout_page = CheckoutPage(driver)

        with allure.step("Open login page and authenticate"):
            login_page.open("https://www.saucedemo.com/")
            login_page.login("standard_user", "secret_sauce")
            login_page.handle_alert_if_present()

        with allure.step("Wait for main page to load"):
            main_page.wait_for_page_load()

        with allure.step("Add products to cart"):
            main_page.add_to_cart("sauce-labs-backpack")
            main_page.add_to_cart("sauce-labs-bolt-t-shirt")
            main_page.add_to_cart("sauce-labs-onesie")

        with allure.step("Navigate to cart"):
            main_page.go_to_cart()
            cart_page.handle_alert_if_present()

        with allure.step("Proceed to checkout"):
            cart_page.click_checkout()

        with allure.step("Fill personal information"):
            checkout_page.fill_personal_data("Диана", "Арсеньева", "123456")
            checkout_page.click_continue()

        with allure.step("Verify total price"):
            total_price = checkout_page.get_total_price()
            expected_total = "58.29"

            with allure.step("Assert total price is correct"):
                assert total_price == expected_total, (
                    f"Ожидалась сумма ${expected_total}, "
                    f"получена: ${total_price}"
                )

        with allure.step("Log successful test completion"):
            print(f"Тест прошел успешно! Итоговая сумма: ${total_price}")

    finally:
        with allure.step("Close browser"):
            driver.quit()


if __name__ == "__main__":
    test_shop_purchase()
