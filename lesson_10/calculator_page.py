from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union


class CalculatorPage:
    """
    Класс для работы со страницей калькулятора.
    Содержит методы для взаимодействия с элементами калькулятора.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def open(self, url: str) -> None:
        """
        Открывает страницу калькулятора по указанному URL.

        Args:
            url: URL страницы для открытия
        """
        self.driver.get(url)

    def set_delay(self, delay_value: Union[int, str]) -> None:
        """
        Устанавливает задержку для операций калькулятора.

        Args:
            delay_value: Значение задержки в секундах
        """
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку калькулятора с указанным текстом.

        Args:
            button_text: Текст кнопки для нажатия
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_result(self) -> str:
        """
        Получает результат вычислений с экрана калькулятора.

        Returns:
            str: Текст результата с экрана калькулятора
        """
        screen = self.driver.find_element(*self.SCREEN)
        return screen.text

    def wait_for_result(self, expected_result: str) -> None:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        Args:
            expected_result: Ожидаемый результат для проверки
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result)
        )
