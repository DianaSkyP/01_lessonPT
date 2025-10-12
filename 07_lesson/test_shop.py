from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage


def test_shop_purchase():

    chrome_options = Options()
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-password-manager-reauthentication")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=chrome_options)

    try:
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        login_page.handle_alert_if_present()

        main_page.wait_for_page_load()

        main_page.add_to_cart("sauce-labs-backpack")
        main_page.add_to_cart("sauce-labs-bolt-t-shirt")
        main_page.add_to_cart("sauce-labs-onesie")

        main_page.go_to_cart()

        cart_page.handle_alert_if_present()

        cart_page.click_checkout()

        checkout_page.fill_personal_data("Диана", "Арсеньева", "123456")
        checkout_page.click_continue()

        total_price = checkout_page.get_total_price()

        expected_total = "58.29"
        assert total_price == expected_total, (
            f"Ожидалась сумма ${expected_total}, получена: ${total_price}"
        )

        print(f"Тест прошел успешно! Итоговая сумма: ${total_price}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shop_purchase()
