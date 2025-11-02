class TestShop:

    def test_shop(self,
                  driver,
                  login_page,
                  products_page,
                  cart_page,
                  checkout_page,
                  overview_page):
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

        assert total_price == "$58.29"
