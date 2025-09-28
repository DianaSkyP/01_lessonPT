from selenium import webdriver
from selenium.webdriver.common.by import By


def test_click_button_with_css_class():
    driver = webdriver.Chrome()

    try:
        driver.get("http://uitestingplayground.com/classattr")

        blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        blue_button.click()

        print("Клик по синей кнопке выполнен успешно!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_click_button_with_css_class()
