from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get('https://www.ya.ru')

sleep(5)

driver.save_screenshot('./ya.png') #сделать скриншот
driver.fullscreen_window()


#driver.back()
#driver.forward()
#driver.refresh()

#driver.set_window_size(640, 480) изменение размера окна

sleep(15)




