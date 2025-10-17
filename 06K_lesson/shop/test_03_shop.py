from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from overview_page import OverviewPage
from products_page import ProductsPage
from shop.login_page import LoginPage


class TestShop:

    def test_shop(self):
        driver = webdriver.Firefox()
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        overview_page = OverviewPage(driver)

        driver.get("https://www.saucedemo.com/")

        login_page.login("standard_user", "secret_sauce")

        products_page.wait_products_page_loaded()
        products_page.add_product_to_cart("backpack")
        products_page.add_product_to_cart("bolt-t-shirt")
        products_page.add_product_to_cart("onesie")
        products_page.go_to_cart()

        cart_page.wait_cart_page_loaded()
        cart_page.go_to_checkout()

        checkout_page.wait_checkout_page_loaded()
        checkout_page.fill_checkout_form("Anastasiia", "Evchuk", "62025")
        checkout_page.push_continue()

        overview_page.wait_summary_total_loaded()
        total_price = overview_page.get_total_price()

        driver.quit()

        assert total_price == "$58.29"
