from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:
    TITLE = By.XPATH, "//*[@data-test='title']"
    FIRST_NAME_INPUT = By.ID, "first-name"
    LAST_NAME_INPUT = By.ID, "last-name"
    ZIP_CODE_INPUT = By.ID, "postal-code"
    CONTINUE_BTN = By.ID, "continue"

    def __init__(self, driver):
        self.driver = driver

    def wait_checkout_page_loaded(self):
        waiter = WebDriverWait(self.driver, 10)
        waiter.until(
            EC.visibility_of_element_located(self.TITLE)
        )

    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE_INPUT).send_keys(zip_code)

    def push_continue(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()
