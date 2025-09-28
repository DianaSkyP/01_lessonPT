from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ajax_button():
    driver = webdriver.Chrome()

    try:
        driver.get("http://uitestingplayground.com/ajax")

        blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
        blue_button.click()

        wait = WebDriverWait(driver, 15)
        green_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success"))
        )

        message_text = green_message.text
        print(f"Текст из зеленой плашки: {message_text}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_ajax_button()
