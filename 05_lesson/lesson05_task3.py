from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('http://the-internet.herokuapp.com/inputs')
search = driver.find_element(By.CSS_SELECTOR,'input')
search.send_keys('Sky')
search.clear()
search.send_keys('Pro')
driver.quit()
