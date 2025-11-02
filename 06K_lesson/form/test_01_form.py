from selenium import webdriver

from form.form import Form


class TestForm:

    def test_form(self):
        driver = webdriver.Edge()
        form = Form(driver)
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        form.wait_form_loaded()
        form.write_first_name("Иван")
        form.write_last_name("Петров")
        form.write_address("Ленина, 55-3")
        form.write_email("test@skypro.com")
        form.write_phone("+7985899998787")
        form.write_city("Москва")
        form.write_country("Россия")
        form.write_job_position("QA")
        form.write_company("SkyPro")
        form.submit()

        zip_color = form.get_color(form.ZIP_CODE_RESULT)
        assert zip_color == "rgba(248, 215, 218, 1)"

        green_fields = [
            form.FIRST_NAME_RESULT,
            form.LAST_NAME_RESULT,
            form.ADDRESS_RESULT,
            form.CITY_RESULT,
            form.COUNTRY_RESULT,
            form.EMAIL_RESULT,
            form.PHONE_RESULT,
            form.JOB_POSITION_RESULT,
            form.COMPANY_RESULT
        ]
        for field in green_fields:
            color = form.get_color(field)
            assert color == "rgba(209, 231, 221, 1)"

        driver.quit()
