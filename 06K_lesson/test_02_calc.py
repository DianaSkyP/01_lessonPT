from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()

    try:
        base_url = "https://bonigarcia.dev/selenium-webdriver-java/"
        url = base_url + "slow-calculator.html"
        driver.get(url)

        wait = WebDriverWait(driver, 50)

        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        screen = driver.find_element(By.CLASS_NAME, "screen")
        result = screen.text
        expected = "15"
        assert result == expected, (
            f"Ожидался результат {expected}, получен: {result}"
        )

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()
