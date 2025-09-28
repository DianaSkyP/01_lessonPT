from selenium import webdriver
from selenium.webdriver.common.by import By


def test_input_field():
    driver = webdriver.Chrome()

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")

        input_field = driver.find_element(By.TAG_NAME, "input")

        input_field.send_keys("Sky")
        print("Введен текст: Sky")

        input_field.clear()
        print("Поле очищено")

        input_field.send_keys("Pro")
        print("Введен текст: Pro")

    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_input_field()
