from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def success_message_contains_product_name(self, name):
        assert self.element_contains_text(name + " has been added to your basket.", *ProductPageLocators.SUCCESS_MESSAGE), \
            "product name do not contains in success message"

    def basket_contains_costs(self, costs):
        assert self.element_contains_text("Basket total: " + costs, *ProductPageLocators.BASKET_SUM), \
            "basket do not have correct costs"

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def success_message_is_not_exist(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "success message is exist"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "success message is not disappeared"
