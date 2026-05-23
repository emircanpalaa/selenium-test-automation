import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False
    })

    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs['driver']
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = os.path.join("screenshots", f"{item.name}.png")
        
        driver.save_screenshot(screenshot_path)