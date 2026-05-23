from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def type_into_field(self, locator, value):
        field = self.wait.until(EC.element_to_be_clickable(locator))
        field.click()
        field.clear()
        field.send_keys(value)

    def fill_information(self, first_name, last_name, postal_code):
        self.type_into_field((By.ID, "first-name"), first_name)
        self.type_into_field((By.ID, "last-name"), last_name)
        self.type_into_field((By.ID, "postal-code"), postal_code)

    def continue_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text
    
    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        ).text