from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        ).click()

    def get_cart_badge_count(self):
        return self.driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_badge"
        ).text

    def remove_backpack_from_cart(self):
        self.driver.find_element(
            By.ID,
            "remove-sauce-labs-backpack"
        ).click()

    def is_cart_badge_not_visible(self):
        cart_badges = self.driver.find_elements(
            By.CLASS_NAME,
            "shopping_cart_badge"
        )

        return len(cart_badges) == 0