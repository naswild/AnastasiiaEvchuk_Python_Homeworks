from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://the-internet.herokuapp.com/login')

username = driver.find_element(By.NAME, 'username')
username.send_keys('tomsmith')

password = driver.find_element(By.NAME, 'password')
password.send_keys('SuperSecretPassword!')

driver.find_element(By.CSS_SELECTOR, 'i').click()

sign = driver.find_element(By.CSS_SELECTOR, '#flash').text
print(sign)

driver.quit()