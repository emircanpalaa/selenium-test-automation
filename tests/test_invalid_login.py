import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username,password,expected_error", [
    ("invalid_user", "invalid_password", "Username and password do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
])
def test_invalid_login(driver, username, password, expected_error):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(username, password)

    error_message = login_page.get_error_message()

    assert expected_error in error_message
    