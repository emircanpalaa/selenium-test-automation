from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

def test_invalid_checkout(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart_page()
    cart_page.click_checkout()

    checkout_page.fill_information("", "", "")
    checkout_page.continue_checkout()

    error_message = checkout_page.get_error_message()

    assert error_message == "Error: First Name is required"
