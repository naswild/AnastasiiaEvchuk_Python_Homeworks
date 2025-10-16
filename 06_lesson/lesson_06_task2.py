from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

NEW_BUTTON_NAME_INPUT = By.ID, "newButtonName"
UPDATING_BUTTON = By.ID, "updatingButton"
new_button_name = "SkyPro"

driver = webdriver.Chrome()
waiter = WebDriverWait(driver,10)
driver.get("http://uitestingplayground.com/textinput")

waiter.until(
    EC.visibility_of_element_located(NEW_BUTTON_NAME_INPUT)
)

driver.find_element(*NEW_BUTTON_NAME_INPUT).send_keys(new_button_name)
driver.find_element(*UPDATING_BUTTON).click()

waiter.until(
    EC.text_to_be_present_in_element(UPDATING_BUTTON, new_button_name)
)

print(driver.find_element(*UPDATING_BUTTON).text)

driver.quit()