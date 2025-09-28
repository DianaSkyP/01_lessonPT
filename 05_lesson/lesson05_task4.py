from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_form():
    driver = webdriver.Chrome()

    try:
        driver.get("http://the-internet.herokuapp.com/login")

        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        print("Введен username: tomsmith")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        print("Введен password: SuperSecretPassword!")

        login_button = driver.find_element(By.CSS_SELECTOR,
                                           "button[type='submit']")
        login_button.click()
        print("Нажата кнопка Login")

        wait = WebDriverWait(driver, 10)
        success_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        message_text = success_message.text
        print(f"Текст с зеленой плашки: {message_text}")

    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_login_form()
