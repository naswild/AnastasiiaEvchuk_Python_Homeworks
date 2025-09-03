from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на labirint
driver.get('https://www.labirint.ru/')

# найти книги по слову Python
search_input = driver.find_element(By.CSS_SELECTOR, '#search-field')
search_input.send_keys('Python', Keys.RETURN)

# собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, 'div.product-card')

# вывести в консоль информацию: название + автор + цена
for book in books:
    author = ''
    title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text
    price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-current').text

    try:
        author = book.find_element(By.CSS_SELECTOR,'div.product-card__author').text
    except:
        author = 'Автор не указан'

    print(f'{author}, "{title}", {price}')

sleep(5)