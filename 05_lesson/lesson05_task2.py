from selenium import webdriver
from selenium.webdriver.common.by import By


def test_click_button_without_id():
    driver = webdriver.Chrome()

    try:
        driver.get("http://uitestingplayground.com/dynamicid")

        xpath = "//button[contains(text(), 'Button with Dynamic ID')]"
        blue_button = driver.find_element(By.XPATH, xpath)
        blue_button.click()

        print("Клик по кнопке с динамическим ID выполнен успешно!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_click_button_without_id()
