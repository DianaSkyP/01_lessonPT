from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Chrome()

    try:
        url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            "button[type='submit']")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        driver.execute_script("arguments[0].click();", submit_button)

        wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        zip_field = driver.find_element(By.ID, "zip-code")
        zip_classes = zip_field.get_attribute("class")
        assert "alert-danger" in zip_classes, (
            f"Zip code должно быть красным, но классы: {zip_classes}"
        )

        green_fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]

        for field_id in green_fields:
            field = driver.find_element(By.ID, field_id)
            field_classes = field.get_attribute("class")
            assert "alert-success" in field_classes, (
                f"Поле {field_id} должно быть зеленым, но классы: "
                f"{field_classes}"
            )

    finally:
        driver.quit()


if __name__ == "__main__":
    test_form()
