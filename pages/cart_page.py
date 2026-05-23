from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        self.driver.find_elements(By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
    