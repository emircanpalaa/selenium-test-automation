import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("first_name,last_name,postal_code,expected_error", [
    ("", "Pala", "34000", "Error: First Name is required"),
    ("Emircan", "", "34000", "Error: Last Name is required"),
    ("Emircan", "Pala", "", "Error: Postal Code is required"),
    ("", "", "", "Error: First Name is required"),
])

def test_invalid_checkout(driver, first_name, last_name, postal_code, expected_error):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart_page()
    cart_page.click_checkout()

    checkout_page.fill_information(first_name, last_name, postal_code)
    checkout_page.continue_checkout()

    error_message = checkout_page.get_error_message()

    assert error_message == expected_error
