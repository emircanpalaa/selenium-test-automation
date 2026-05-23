from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class InventoryPage(BasePage):

    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    LOGIN_BUTTON = (By.ID, "login-button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART)

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def remove_backpack_from_cart(self):
        self.click((By.ID, "remove-sauce-labs-backpack"))

    def is_cart_badge_not_visible(self):
        cart_badges = self.driver.find_elements(*self.CART_BADGE)

        return len(cart_badges) == 0
    
    def go_to_cart_page(self):
        self.click((By.CLASS_NAME, "shopping_cart_link"))

    def open_menu(self):
        self.click((By.ID, "react-burger-menu-btn"))

    def click_logout(self):
       self.click((By.ID, "logout_sidebar_link"))
       
    def add_bike_light_to_cart(self):
        self.click((By.ID, "add-to-cart-sauce-labs-bike-light"))