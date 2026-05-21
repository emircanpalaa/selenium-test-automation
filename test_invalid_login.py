from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_invalid_login(driver):

    driver.get("https://www.saucedemo.com/")
    
    login_page = LoginPage(driver)

    login_page.login("invalid_user", "invalid_password")

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text

    assert "Username and password do not match any user in this service" in error_message

    print("Hatali Login Basarili")

    driver.quit()