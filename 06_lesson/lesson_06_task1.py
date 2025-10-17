from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

AJAX_BUTTON = By.ID, "ajaxButton"
SUCCESS_MESSAGE = By.CSS_SELECTOR, ".bg-success"

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 20)
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(*AJAX_BUTTON).click()

waiter.until(
    EC.visibility_of_element_located(SUCCESS_MESSAGE)
)

print(driver.find_element(*SUCCESS_MESSAGE).text)

driver.quit()