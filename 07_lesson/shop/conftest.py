import pytest
from selenium import webdriver

from shop.cart_page import CartPage
from shop.checkout_page import CheckoutPage
from shop.login_page import LoginPage
from shop.overview_page import OverviewPage
from shop.products_page import ProductsPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def products_page(driver):
    return ProductsPage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def checkout_page(driver):
    return CheckoutPage(driver)


@pytest.fixture()
def overview_page(driver):
    return OverviewPage(driver)
