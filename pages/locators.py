from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CSS_SELECTOR, ".basket-mini .btn-default")


class CartPageLocators(object):
    ITEMS_LIST = (By.CSS_SELECTOR, "#content_inner")
    ITEM = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    BASKET_SUM = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p")
