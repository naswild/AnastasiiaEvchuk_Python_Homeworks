from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Вывод заголовка в консоль
# driver.get('https://www.example.com/')
# header = driver.find_element(By.CSS_SELECTOR, 'h1').text
# print(header)

#Нажатие на кнопку Donate
# driver.get('https://www.python.org/')
# driver.find_element(By.CSS_SELECTOR, '.donate-button').click()
#или driver.find_element(By.LINK_TEXT, "Donate").click()
# sleep(10)

# Поиск в гугл
driver.get('https://www.google.com/')
sleep(5)
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('photos', Keys.RETURN)

sleep(5)