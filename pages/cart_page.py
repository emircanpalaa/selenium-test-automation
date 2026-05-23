from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEM)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
    