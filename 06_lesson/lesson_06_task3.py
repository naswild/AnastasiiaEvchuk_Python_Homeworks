from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

STATUS_MSG = By.ID, "text"
IMAGE_CONTAINER = By.ID, "image-container"

driver = webdriver.Chrome()
waiter = WebDriverWait(driver,10)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(
    EC.text_to_be_present_in_element(STATUS_MSG, "Done!")
)

list_of_images = driver.find_element(*IMAGE_CONTAINER).find_elements(By.TAG_NAME, "img")

print(list_of_images[2].get_attribute("src"))

driver.quit()
