from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.USERNAME_FIELD)
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def handle_alert_if_present(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception:
            pass


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located(self.INVENTORY_LIST))

    def add_to_cart(self, product_name):
        product_id = product_name.lower().replace(" ", "-")
        add_button_id = f"add-to-cart-{product_id}"
        add_button = self.driver.find_element(By.ID, add_button_id)
        add_button.click()

    def go_to_cart(self):
        cart_link = self.driver.find_element(*self.CART_LINK)
        cart_link.click()


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()

    def get_cart_items_count(self):
        cart_items = self.driver.find_elements(*self.CART_ITEMS)
        return len(cart_items)

    def handle_alert_if_present(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception:
            pass


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def fill_personal_data(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        postal_field = self.driver.find_element(*self.POSTAL_CODE_FIELD)
        postal_field.send_keys(postal_code)

    def click_continue(self):
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()

    def get_total_price(self):
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_PRICE)
        )
        total_text = total_element.text
        return total_text.split("$")[1] if "$" in total_text else total_text
