from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    TITLE = By.XPATH, "//*[@data-test='title']"
    CHECKOUT_BTN = By.ID, "checkout"

    def __init__(self, driver):
        self.driver = driver

    def wait_cart_page_loaded(self):
        waiter = WebDriverWait(self.driver, 10)
        waiter.until(
            EC.visibility_of_element_located(self.TITLE)
        )

    def go_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()
