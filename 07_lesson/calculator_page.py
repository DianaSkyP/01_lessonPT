from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, delay_value):
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_button(self, button_text):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_result(self):
        screen = self.driver.find_element(*self.SCREEN)
        return screen.text

    def wait_for_result(self, expected_result):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result)
        )
