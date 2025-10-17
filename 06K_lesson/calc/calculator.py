from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Calculator:
    DELAY = By.CSS_SELECTOR, "#delay"
    RESULT = By.CSS_SELECTOR, ".screen"

    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, sec: str):
        self.driver.find_element(*self.DELAY).clear()
        self.driver.find_element(*self.DELAY).send_keys(sec)

    def push_btn(self, btn):
        self.driver.find_element(By.XPATH, f"//*[text()='{btn}']").click()

    def wait_result(self, result: str):
        waiter = WebDriverWait(self.driver, int(result) + 5)
        waiter.until(EC.text_to_be_present_in_element(self.RESULT, result))
