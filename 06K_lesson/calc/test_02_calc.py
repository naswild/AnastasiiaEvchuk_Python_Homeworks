import time

from selenium import webdriver
from calc.calculator import Calculator


class TestCalculator:

    def test_calculator(self):
        driver = webdriver.Chrome()
        calculator = Calculator(driver)
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        delay = "45"
        calculator.set_delay(delay)
        calculator.push_btn("7")
        calculator.push_btn("+")
        calculator.push_btn("8")
        calculator.push_btn("=")
        start_time = time.time()
        calculator.wait_result("15")
        end_time = time.time()
        elapsed_time = int(end_time - start_time)

        assert elapsed_time == int(delay)

        driver.quit()
