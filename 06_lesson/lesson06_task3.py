from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_wait_for_images():
    driver = webdriver.Chrome()

    try:
        base_url = "https://bonigarcia.dev/selenium-webdriver-java/"
        url = base_url + "loading-images.html"
        driver.get(url)

        wait = WebDriverWait(driver, 20)

        wait.until(
            lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3
        )

        wait.until(
            lambda d: all(
                img.get_attribute("src") and img.get_attribute("src") != ""
                for img in d.find_elements(By.TAG_NAME, "img")[:3]
            )
        )

        all_images = driver.find_elements(By.TAG_NAME, "img")

        if len(all_images) >= 3:
            third_image_src = all_images[2].get_attribute("src")
            message = (f"Значение атрибута src у 3-й картинки: "
                       f"{third_image_src}")
            print(message)
        else:
            message = (f"Найдено только {len(all_images)} картинок, "
                       f"а нужно минимум 3")
            print(message)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_wait_for_images()
