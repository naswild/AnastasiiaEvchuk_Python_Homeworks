from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OverviewPage:
    SUMMARY_TOTAL = By.XPATH, "//*[@data-test='total-label']"

    def __init__(self, driver):
        self.driver = driver

    def wait_summary_total_loaded(self):
        waiter = WebDriverWait(self.driver, 10)
        waiter.until(
            EC.visibility_of_element_located(self.SUMMARY_TOTAL))

    def get_total_price(self):
        total_price = self.driver.find_element(*self.SUMMARY_TOTAL).text
        return total_price.split()[-1]
