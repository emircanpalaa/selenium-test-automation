from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def test_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )

    assert "inventory" in driver.current_url