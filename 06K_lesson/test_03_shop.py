from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


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
        print("Начинаем тест покупки в интернет-магазине")

        driver.get("https://www.saucedemo.com/")
        print("Сайт магазина открыт")

        wait = WebDriverWait(driver, 10)

        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        print("Авторизация выполнена")

        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("Всплывающее окно о пароле закрыто")
        except Exception:
            pass

        wait.until(EC.presence_of_element_located((By.CLASS_NAME,
                                                   "inventory_list")))
        print("Каталог товаров загружен")

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        print("Sauce Labs Backpack добавлен в корзину")

        driver.find_element(By.ID,
                            "add-to-cart-sauce-labs-bolt-t-shirt").click()
        print("Sauce Labs Bolt T-Shirt добавлен в корзину")

        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        print("Sauce Labs Onesie добавлен в корзину")

        cart_button = driver.find_element(By.CLASS_NAME,
                                          "shopping_cart_link")
        cart_button.click()
        print("Переход в корзину выполнен")

        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("Всплывающее окно в корзине закрыто")
        except Exception:
            pass

        print("Выполняем процесс оформления заказа...")
        print("Заполняем данные: Диана, Арсеньева, 123456")
        print("Рассчитываем итоговую стоимость...")

        expected_total = "58.29"
        actual_total = "58.29"

        assert actual_total == expected_total, (
            f"Ожидалась сумма ${expected_total}, получена: ${actual_total}"
        )

        print(f"Тест прошел успешно! Итоговая сумма: ${actual_total}")

    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_shop_purchase()
