from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def is_not_have_items(self):
        assert self.is_not_element_present(*CartPageLocators.ITEM), \
            "there are product in basket"

    def has_empty_items_message(self):
        assert self.element_contains_text("Your basket is empty.", *CartPageLocators.ITEMS_LIST), \
            "basket is not empty"
