from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

        self.driver.find_element(By.ID, "user-name").send_keys(username)

        self.driver.find_element(By.ID, "password").send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )

        login_button.click()