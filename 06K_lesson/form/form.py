from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Form:
    ALL_ELEMENTS_LOCATOR = By.CSS_SELECTOR, ".form-label"
    FIRST_NAME_INPUT = By.NAME, "first-name"
    LAST_NAME_INPUT = By.NAME, "last-name"
    ADDRESS_INPUT = By.NAME, "address"
    ZIP_CODE_INPUT = By.NAME, "zip-code"
    CITY_INPUT = By.NAME, "city"
    COUNTRY_INPUT = By.NAME, "country"
    EMAIL_INPUT = By.NAME, "e-mail"
    PHONE_INPUT = By.NAME, "phone"
    JOB_POSITION_INPUT = By.NAME, "job-position"
    COMPANY_INPUT = By.NAME, "company"
    SUBMIT_BTN = By.CSS_SELECTOR, "[type='submit']"

    FIRST_NAME_RESULT = By.ID, "first-name"
    LAST_NAME_RESULT = By.ID, "last-name"
    ADDRESS_RESULT = By.ID, "address"
    ZIP_CODE_RESULT = By.ID, "zip-code"
    CITY_RESULT = By.ID, "city"
    COUNTRY_RESULT = By.ID, "country"
    EMAIL_RESULT = By.ID, "e-mail"
    PHONE_RESULT = By.ID, "phone"
    JOB_POSITION_RESULT = By.ID, "job-position"
    COMPANY_RESULT = By.ID, "company"

    def __init__(self, driver):
        self.driver = driver

    def wait_form_loaded(self):
        waiter = WebDriverWait(self.driver, 10)
        waiter.until(
            EC.visibility_of_all_elements_located(self.ALL_ELEMENTS_LOCATOR)
        )

    def write_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def write_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def write_address(self, address):
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def write_zip_code(self, zip_code):
        self.driver.find_element(*self.ZIP_CODE_INPUT).send_keys(zip_code)

    def write_city(self, city):
        self.driver.find_element(*self.CITY_INPUT).send_keys(city)

    def write_country(self, country):
        self.driver.find_element(*self.COUNTRY_INPUT).send_keys(country)

    def write_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def write_phone(self, phone):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def write_job_position(self, job_position):
        self.driver.find_element(*self.JOB_POSITION_INPUT).send_keys(job_position)

    def write_company(self, company):
        self.driver.find_element(*self.COMPANY_INPUT).send_keys(company)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def get_color(self, locator):
        color = self.driver.find_element(*locator).value_of_css_property("background-color")
        return color
