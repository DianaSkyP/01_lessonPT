from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_rename_button():
    driver = webdriver.Chrome()

    try:
        driver.get("http://uitestingplayground.com/textinput")

        input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
        input_field.send_keys("SkyPro")

        blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
        blue_button.click()

        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "#updatingButton"), "SkyPro"
            )
        )

        button_element = driver.find_element(By.CSS_SELECTOR,
                                             "#updatingButton")
        button_text = button_element.text
        print(f"Текст кнопки: {button_text}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_rename_button()
