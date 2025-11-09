import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture()
def calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator = CalculatorPage(driver)
    yield calculator
    driver.quit()
