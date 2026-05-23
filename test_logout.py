from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_logout(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.open_menu()
    inventory_page.click_logout()

    assert driver.current_url == "https://www.saucedemo.com/"