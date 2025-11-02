from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductsPage:
    TITLE = By.XPATH, "//*[@data-test='title']"
    CART_BTN = By.XPATH, "//*[@data-test='shopping-cart-link']"

    def __init__(self, driver):
        self.driver = driver

    def wait_products_page_loaded(self):
        waiter = WebDriverWait(self.driver, 10)
        waiter.until(
            EC.visibility_of_element_located(self.TITLE)
        )

    def add_product_to_cart(self, product):
        self.driver.find_element(By.ID, f"add-to-cart-sauce-labs-{product}").click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_BTN).click()
